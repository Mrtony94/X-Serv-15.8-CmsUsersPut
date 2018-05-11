from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^accounts/profile/$', 'cmsusersput.views.usuario'),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^cmsusersput/$', 'cmsusersput.views.dame_paginas'),
    url(r'^cmsusersput/(.+)/(.*)', 'cmsusersput.views.paginanueva'),
    url(r'^cmsusersput/(\d+)', 'cmsusersput.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
