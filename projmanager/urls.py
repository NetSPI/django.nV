from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^taskManager/', include('taskManager.urls', namespace="taskManager")),
    url(r'^admin/', include(admin.site.urls)),
) 