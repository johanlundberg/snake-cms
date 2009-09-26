from django.conf.urls.defaults import *
from snakelog.models import Entry

entry_info_dict = {
    'queryset': Entry.live.all(), # Uses LiveEntryManager
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$', 'archive_index', entry_info_dict, 'snakelog_entry_archive_index'),
    (r'^(?P<year>\d{4})/$', 'archive_year',
         entry_info_dict, 'snakelog_entry_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
         'archive_month', entry_info_dict, 'snakelog_entry_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
         'archive_day', entry_info_dict, 'snakelog_entry_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-w\w]+)/$',
         'object_detail', entry_info_dict, 'snakelog_entry_detail'),
)