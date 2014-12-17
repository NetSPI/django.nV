from django.contrib import admin
from taskManager.models import Task, Project, Notes

# Register your models here.

class CommentInline(admin.TabularInline):
	model = Notes
	extra = 3	

class TaskInline(admin.TabularInline):
	model = Task
	extra = 4

class TaskAdmin(admin.ModelAdmin):
	fields = ['getProjectTitle','pub_date', 'task_text']
	inlines = [CommentInline]
	search_fields = ['task_text', 'getProjectTitle']
	list_display = ('getProjectTitle','task_text', 'pub_date', 'was_created_recently')

class ProjectAdmin(admin.ModelAdmin):
	fields = ['start_date', 'project_text', 'project_title']
	inlines = [TaskInline]
	search_fields = ['project_text']
	list_display = ('project_title', 'project_text', 'start_date', 'was_created_recently')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Notes)