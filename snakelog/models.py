import datetime

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from tagging.fields import TagField
from markdown import markdown

class Category(models.Model):
	title = models.CharField(max_length=250,
							 help_text='Maximum 250 characters.')
	description = models.TextField()
	slug = models.SlugField(unique=True, help_text='Suggested value \
							#automatically generated from title. Must be unique.')

	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return('snakelog_category_detail', (),
			   {'slug': self.slug})
	get_absolute_url = models.permalink(get_absolute_url)

	def live_entry_set(self):
		from snakelog.models import Entry
		return self.entry_set.filter(status=Entry.LIVE_STATUS)

# The Manager have to be created before used in the Entry class
class LiveEntryManager(models.Manager):
	def get_query_set(self):
		return super(LiveEntryManager, self).get_query_set().filter(
												status=self.model.LIVE_STATUS)

class Entry(models.Model):
	LIVE_STATUS = 0
	DRAFT_STATUS = 1
	HIDDEN_STATUS = 2
	STATUS_CHOICES = (
				  (LIVE_STATUS, 'Live'),
				  (DRAFT_STATUS, 'Draft'),
				  (HIDDEN_STATUS, 'Hidden'),
				  )

	# Core fields
	title = models.CharField(max_length=250)
	excerpt = models.TextField(blank=True)
	body = models.TextField()
	pub_date = models.DateTimeField(default=datetime.datetime.now)

	# Fields to store generated HTML
	excerpt_html = models.TextField(editable = False, blank=True)
	body_html = models.TextField(editable = False, blank=True)

	# Metadata
	author = models.ForeignKey(User)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	slug = models.SlugField(unique_for_date='pub_date')
	status = models.IntegerField(choices=STATUS_CHOICES, default = LIVE_STATUS)

	# Categorization
	categories = models.ManyToManyField(Category)
	tags = TagField(help_text="Separate tags with spaces")

	# Database queries
	objects = models.Manager() # The first one is default (admin interface uses this one)
	live = LiveEntryManager()

	class Meta:
		verbose_name_plural = "Entries"
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.title

	def save(self):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html = markdown(self.excerpt)
		super(Entry, self).save()

	# An alternative to get_absolute_url = models.permalink(get_absolute_url) is
	# @models.permalink above this function
	def get_absolute_url(self):
		return ('snakelog_entry_detail', (), {'year': self.pub_date.strftime("%Y"),
											 'month': self.pub_date.strftime("%b").lower(),
											 'day': self.pub_date.strftime("%d"),
											 'slug': self.slug })
	get_absolute_url = models.permalink(get_absolute_url)

# Comment moderator for the Entry model
from django.contrib.comments.moderation import CommentModerator, moderator
class EntryModerator(CommentModerator):
	email_notification = True
	enable_field = 'enable_comments'
	auto_moderate_field ='pub_date'
	# Auto moderate 14 days after pub_date
	moderate_after = 14
moderator.register(Entry, EntryModerator)

# Code from
# http://sciyoshi.com/blog/2008/aug/27/using-akismet-djangos-new-comments-framework/
from django.contrib.comments.signals import comment_was_posted
def on_comment_was_posted(sender, comment, request, *args, **kwargs):
    # spam checking can be enabled/disabled per the comment's target Model
    #if comment.content_type.model_class() != Entry:
    #    return

    from django.contrib.sites.models import Site
    from django.conf import settings

    try:
        from akismet import Akismet
    except:
        return

    # use TypePad's AntiSpam if the key is specified in settings.py
    if hasattr(settings, 'TYPEPAD_ANTISPAM_API_KEY'):
        ak = Akismet(
            key=settings.TYPEPAD_ANTISPAM_API_KEY,
            blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )
        ak.baseurl = 'api.antispam.typepad.com/1.1/'
    else:
        ak = Akismet(
            key=settings.AKISMET_API_KEY,
            blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
        )

    if ak.verify_key():
        data = {
            'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
            'user_agent': request.META.get('HTTP_USER_AGENT', ''),
            'referrer': request.META.get('HTTP_REFERER', ''),
            'comment_type': 'comment',
            'comment_author': comment.user_name.encode('utf-8'),
        }

        if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
            comment.flags.create(
                user=comment.content_object.author,
                flag='spam'
            )
            comment.is_public = False
            comment.save()
comment_was_posted.connect(on_comment_was_posted)

class Link(models.Model):
	# Core fields
	title = models.CharField(max_length=250)
	url = models.URLField(unique=True)
	description = models.TextField(blank=True)
	description_html = models.TextField(editable = False, blank=True)
	pub_date = models.DateTimeField(default=datetime.datetime.now)

	# Meta data
	slug = models.SlugField(unique_for_date='pub_date',
						    help_text = 'Must be unique for the publication date.')
	via_name = models.CharField('Via', max_length=250, blank=True,
		help_text='The name of the person whose site you spotted the link on. Optional.')
	via_url = models.URLField('Via URL', blank=True,
		help_text = 'The URL of the site where you spotted the link. Optional.')
	tags = TagField(help_text="Separate tags with spaces")
	post_elsewhere = models.BooleanField('Post to del.icio.us', default=True,
		help_text = 'If checked, this link will be posted both to your weblog and \
										to your del.icio.us account.')
	enable_comments = models.BooleanField(default=True)
	posted_by = models.ForeignKey(User)

	class Meta:
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.title

	def save(self):
		if self.description:
			self.description_html = markdown(self.description)
		if not self.id and self.post_elsewhere:
			import pydelicious
			from django.utils.encoding import smart_str
			pydelicious.add(settings.DELICIOUS_USER, settings.DELICIOUS_PASSWORD,
						    smart_str(self.url), smart_str(self.title),
						    smart_str(self.tags))
		super(Link, self).save()

	def get_absolute_url(self):
		return ('snakelog_link_detail', (), {'year': self.pub_date.strftime("%Y"),
										 'month': self.pub_date.strftime("%b").lower(),
										 'day': self.pub_date.strftime("%d"),
										 'slug': self.slug })
	get_absolute_url = models.permalink(get_absolute_url)