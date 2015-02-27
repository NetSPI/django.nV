from django.conf.urls import patterns, url

from taskManager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name = 'logout_user'),
    url(r'^(?P<project_id>\d+)/$', views.proj_details, name = 'proj_details'),
    url(r'^(?P<project_id>\d+)/newtask/$', views.newtask, name = 'new_task'),
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/$', views.task_details, name = 'task_details'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.login_view, name = 'login'),
    url(r'^newproj/$', views.newproj, name= 'new project'),
    url(r'^manage_groups/$', views.manageGroups, name = 'manage_groups'),
    url(r'^manage_projects/$', views.manageProjects, name = 'manage_projects'),
    url(r'^(?P<project_id>\d+)/manage_tasks/$', views.manageTasks, name = 'manage_tasks'),
    url(r'^(?P<project_id>\d+)/delete_project/$', views.deleteProject, name = 'delete_project'),
	url(r'^dashboard/$', views.dashboard, name = 'dashboard'),
	url(r'^profile/$', views.profile, name = 'profile'),
	url(r'^tutorials/$', views.tutorials, name = 'tutorials'),
	url(r'^tutorials/(?P<vuln_id>[a-z\-]+)/$', views.show_tutorial, name = 'show_tutorial'),
	
)