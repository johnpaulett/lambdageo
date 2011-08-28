from django.conf.urls.defaults import patterns, include, url
from django.contrib.gis import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    'geo.views',
    url(r'^$', 'index'),
    url(r'^building/(?P<building_id>\d+)/$', 'building_detail', name='building'),
    url(r'^upload/', 'upload'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
