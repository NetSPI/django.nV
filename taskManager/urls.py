from django.conf.urls import patterns, url

from taskManager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_view, name = 'logout_user'),
    url(r'^(?P<project_id>\d+)/$', views.proj_details, name = 'proj_details'),
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/$', views.detail, name = 'detail'),
    url(r'^thanks/$', views.thanks, name = 'thanks'),
    url(r'^(?P<task_id>\d+)/comments/$', views.the_comments, name='comments'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.login_view, name = 'login'),
)