from django.conf.urls.defaults import *
from snakelog.models import Entry, Link
from tagging.models import Tag

urlpatterns = patterns('',
    (r'^$',
        'django.views.generic.list_detail.object_list',
        {'queryset': Tag.objects.all()}, 'snakelog_tag_list'),
    (r'^entries/(?P<tag>[-\w]+)/$',
        'tagging.views.tagged_object_list',
        {'queryset_or_model': Entry.live.all(), # Uses LiveEntryManager
        'template_name': 'snakelog/entries_by_tag.html'}),
    (r'^links/(?P<tag>[-\w]+)/$',
        'tagging.views.tagged_object_list',
        {'queryset_or_model': Link,
        'template_name': 'snakelog/links_by_tag.html'}),
)