from django.conf.urls.defaults import *
from snakelog.models import Category

urlpatterns = patterns('',
    (r'^$',
        'django.views.generic.list_detail.object_list',
        {'queryset': Category.objects.all()}, 'snakelog_category_list'),
    url(r'^(?P<slug>[-\w]+)/$',
        'snakelog.views.category_detail',
        name='snakelog_category_detail'),
)