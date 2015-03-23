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
	priority = models.IntegerField(default = 1)

	def __str__(self):
		return self.project_title

	def was_created_recently(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days =1)

	def percent_complete(self):
		counter = 0
		for a in self.task_set.all():
			counter = counter + (1 if a.completed else 0)
		try:
			return round(float(counter) / self.task_set.count() * 100)
		except:
			return 0

class Task(models.Model):
	assoc_project = models.ForeignKey(Project, default=1)
	task_text = models.CharField(max_length = 200)
	title = models.CharField(max_length = 200, default="N/A")
	pub_date = models.DateTimeField('date created')
	due_date = models.DateTimeField('date due', default=(timezone.now() + datetime.timedelta(weeks=1)))
	completed = models.NullBooleanField(default = False)
	users_assigned = models.ManyToManyField(User)

	def __str__(self):
		return self.task_text

	def getProjectTitle(self):
		return self.assoc_project.project_title

	def was_created_recently(self):
		return self.pub_date >=timezone.now() - datetime.timedelta(days =1)

	def is_overdue(self):
		return self.due_date <= timezone.now()

class Notes(models.Model):
	task = models.ForeignKey(Task, default=1)
	title = models.CharField(max_length = 200, default = "N/A")
	note_text = models.CharField(max_length = 200)
	image_url = models.CharField(max_length = 200)
	user = models.CharField(max_length = 200, default = 'ancestor')

	def __str__(self):
		return self.note_text

class File(models.Model):
	project = models.ForeignKey(Project)
	name = models.CharField(max_length=300, default="")
	path = models.CharField(max_length=3000, default="")

	def __str__(self):
		return self.name