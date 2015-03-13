from django.conf.urls.defaults import patterns, include, url

from django.views.static import * 
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'home.views.home'),
    url(r'^home/$', 'home.views.home'),
    url(r'^home/(?P<categorie>\w+)/(?P<chapter>\w+(-\w+)*\d*)/$', 'home.views.home'),                   
    url(r'^about/$', 'home.views.about'),
    url(r'^fsignup/$', 'home.views.fsignup'),
    url(r'^fsignin/$', 'home.views.login'),
    url(r'^logout/$', 'home.views.logout'),
    url(r'login/$', 'home.views.login'),
    url(r'^dev/(?P<chapter>\w+(-\w+)*\d*)/$', 'home.views.dev'),                   
    url(r'^dev/$', 'home.views.dev'),                   
    url(r'^home/(?P<categorie>\w+)/(?P<chapter>\w+(-\w+)*\d*)/set_user_slide/$', 'home.views.user_slide'),              
    url(r'^home/(?P<categorie>\w+)/(?P<chapter>\w+(-\w+)*\d*)/set_user_post/$', 'home.views.user_post'),

    url(r'database/$', 'home.views.database'),

            
    # Examples:
    # url(r'^$', 'cpp.views.home', name='home'),
    # url(r'^cpp/', include('cpp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls))
)
