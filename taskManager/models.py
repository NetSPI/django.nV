import datetime

from django.contrib.auth.models import User

from django.utils import timezone
from django.db import models
from django import forms

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	profile_img = models.TextField()

class Project(models.Model):
	project_title = models.CharField(max_length = 50, default = 'Default')
	project_text = models.CharField(max_length = 500)
	start_date = models.DateTimeField('date started')
	users_assigned = models.ManyToManyField(User)

	def __str__(self):
		return self.project_title

	def was_created_recently(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days =1)


class Task(models.Model):
	assoc_project = models.ForeignKey(Project, default=1)
	task_text = models.CharField(max_length = 200)
	title = models.CharField(max_length = 200, default="N/A")
	pub_date = models.DateTimeField('date created')
	completed = models.NullBooleanField(default = False)
	users_assigned = models.ManyToManyField(User)

	def __str__(self):
		return self.task_text

	def getProjectTitle(self):
		return self.assoc_project.project_title

	def was_created_recently(self):
		return self.pub_date >=timezone.now() - datetime.timedelta(days =1)

class Notes(models.Model):
	task = models.ForeignKey(Task, default=1)
	title = models.CharField(max_length = 200, default = "N/A")
	note_text = models.CharField(max_length = 200)
	image_url = models.CharField(max_length = 200)
	user = models.CharField(max_length = 200, default = 'ancestor')

	def __str__(self):
		return self.note_text