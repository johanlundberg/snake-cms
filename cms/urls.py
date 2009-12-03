from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin URLs
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    #(r'^tinymce/', include('tinymce.urls')),
    (r'^admin/(.*)', admin.site.root),
    # cms URLs
    (r'^/?$', 'django.views.generic.simple.redirect_to', { 'url': 'weblog/' } ),
    (r'^search/$', 'cms.search.views.search'),
    # snakelog URLs
    (r'^weblog/categories/', include('snakelog.urls.categories')),
    (r'^weblog/links/', include('snakelog.urls.links')),
    (r'^weblog/tags/', include('snakelog.urls.tags')),
    (r'^weblog/', include('snakelog.urls.entries')),
    # Comment URLS
    (r'^comments/', include('django.contrib.comments.urls')),
    # Last catch all for flatpages
    (r'', include('django.contrib.flatpages.urls')),
)
