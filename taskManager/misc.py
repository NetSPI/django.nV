import os

def store_uploaded_file(title, f):
	d = '%s/static/taskManager/uploads' % (os.path.dirname(os.path.realpath(__file__)))
	if not os.path.exists(d):
		os.makedirs(d)
	with open('%s/static/taskManager/uploads/%s' % (os.path.dirname(os.path.realpath(__file__)), title), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	return '/static/taskManager/uploads/%s' % (title)

def get_my_choices_users():
	# you place some logic here
	user_list = User.objects.order_by('date_joined')
	user_tuple = []
	counter = 1
	for user in user_list:
		user_tuple.append((counter, user))
		counter = counter +1
	return user_tuple


def get_my_choices_projects():
	# you place some logic here
	proj_list = Project.objects.all()
	proj_tuple = []
	counter = 1
	for proj in proj_list:
		proj_tuple.append((counter, proj))
		counter = counter +1
	return proj_tuple

def get_my_choices_tasks(current_proj):
	# you place some logic here
	task_list = []
	tasks = Task.objects.all()
	# for task in tasks:
	#     if task.project == current_proj:
	#         task_list.append(task)
	task_tuple = []
	counter = 1
	for task in tasks:
		task_tuple.append((counter, task))
		counter = counter +1
	return task_tuple