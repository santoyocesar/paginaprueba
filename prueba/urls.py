from django.conf.urls import patterns, include, url

from prueba.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^hello/$',hello),
    #url(r'^time/$',current_datetime),
    url(r'^home/$',home),
    url(r'^news/$',news),
    url(r'^about/$',about),
    #url(r'^admin/', include(admin.site.urls)),
)
