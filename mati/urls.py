
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('mati.views',


    url(r'^$', 'index', name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # urls de autenticacion de usuario
    url(r'^accounts/login/$',  'login', name='login'),
    url(r'^accounts/auth/$',  'auth_view', name='auth_view'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
    url(r'^accounts/loggedin/$', 'loggedin', name='loggedin'),
    url(r'^accounts/invalid/$', 'invalid_login', name='invalid_login'),
    url(r'^accounts/register/$', 'register_user', name='register_user'),
    url(r'^accounts/register_success/$', 'register_success', name='register_success'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/', include('map.urls')),
    url(r'^dimaps/', include('dimaps.urls')),
)


# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'pensum', pensum_views_drf.PensumViewSet)
# router.register(r'users', pensum_views_drf.UserViewSet)

    # Examples:
    # url(r'^$', 'mati.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #	url(r'^about/$', ('about'), name='about'),
    #url(r'^sign_in/$', ('sign_in'), name='sign_in'),
    #url(r'^sign_up/$', ('sign_up'), name='sign_up'),

    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
