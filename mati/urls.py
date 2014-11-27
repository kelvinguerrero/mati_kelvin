from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mati.views',
    # Examples:
    # url(r'^$', 'mati.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index', name='index'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/', include('map.urls')),
    url(r'^dimaps/', include('dimaps.urls')),
)
