import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.views.generic import RedirectView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, Permission, User
from taskManager.forms import UserForm, GroupForm, AssignProject, ManageTask
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import connection
from django.contrib import messages
from taskManager.models import Task, Project, Notes

#20821e4abaea95268880f020c9f6768288f3725a
#add completed status, due date
#pmem can only see his tasks
#pman can only see his projects
#admin can see all tasks

def manageTasks(request, project_id):

	print('here')
	user  = request.user
	proj = Project.objects.get(pk = project_id)

	if user.is_authenticated():
		logged_in = True

		if user.has_perm('can_change_project'):

			if request.method == 'POST':
				form = ManageTask(request.POST)
				valid = False
				if form.is_valid():
					valid = True
					username_input = form.cleaned_data['User']
					task_input = form.cleaned_data['Task']

					user_tuples = get_my_choices_users()
					task_tuples = get_my_choices_tasks(proj)

					user = User.objects.get(username= user_tuples[int(username_input)-1][1])
					task = Task.objects.get(task_text = task_tuples[int(task_input)-1][1])

					task.users_assigned.add(user)
					
				return render_to_response('taskManager/manage_tasks.html', 
					{'task':form.errors, 'valid':valid, 'logged_in':logged_in}, RequestContext(request))

			else:   
				form = ManageTask(current_proj = proj)

				return render_to_response('taskManager/manage_tasks.html', 
					{'form':form,'logged_in':logged_in}, RequestContext(request))

		else:
			return redirect('/taskManager/', {'permission':False})
	else:
		redirect('/taskManager/', {'logged_in':False})


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
	#     if task.assoc_project == current_proj:
	#         task_list.append(task)
	task_tuple = []
	counter = 1
	for task in tasks:
		task_tuple.append((counter, task))
		counter = counter +1
	return task_tuple


def manageProjects(request):

	user  = request.user

	if user.is_authenticated():
		logged_in = True

		if user.has_perm('can_change_group'):

			if request.method == 'POST':
				form = AssignProject(request.POST)
				if form.is_valid():

					username_input = form.cleaned_data['User']
					project_title_input = form.cleaned_data['Project']

					user_tuples = get_my_choices_users()
					project_tuples = get_my_choices_projects()

					user = User.objects.get(username=user_tuples[int(username_input)-1][1])
					project = Project.objects.get(project_title = project_tuples[int(project_title_input)-1][1])

					project.users_assigned.add(user)

				return redirect('/taskManager/')
			else:   

				form = AssignProject()

				return redirect('/taskManager/')

		else:
			return redirect('/taskManager/', {'permission':False})
	else:
		redirect('/taskManager/', {'logged_in':False})

def deleteProject(request, project_id):
	# IDOR
	project = Project.objects.get(pk=project_id)
	project.delete()
	return redirect('/taskManager/dashboard')

def manageGroups(request):

	user  = request.user

	if user.is_authenticated():
		logged_in = True

		if user.has_perm('can_change_group'):
			
			user_list = User.objects.order_by('date_joined')

			if request.method == 'POST':

				selected_choice = request.POST.dict()

				counter = 1
				groups_changed = False

				while counter < len(selected_choice):

					current = "radio" + str(counter)
					current_bool = "radio_bool" + str(counter)
					
					if current in selected_choice.keys() and current_bool in selected_choice.keys():

						user_list[counter-1].groups.clear()

						if selected_choice[current] == 'admin_g':
							grp = Group.objects.get(name='admin_g')
							user_list[counter-1].groups.add(grp)#admin group
							groups_changed = True
						elif selected_choice[current] == 'project_managers':
							grp = Group.objects.get(name='project_managers')
							user_list[counter-1].groups.add(grp)#manager  group                     
							groups_changed = True
						elif selected_choice[current] == 'team_member':
							grp = Group.objects.get(name='team_member')
							user_list[counter-1].groups.add(grp)
							groups_changed = True

						user_list[counter-1].save()

					counter = counter+1

				return render_to_response('taskManager/manage_groups.html', 
					{'users':user_list,'choices':selected_choice, 'groups_changed':groups_changed, 'logged_in':logged_in}, RequestContext(request))

			else:	
				return render_to_response('taskManager/manage_groups.html', 
					{'users':user_list, 'logged_in':logged_in}, RequestContext(request))
		else:
			return redirect('/taskManager/', {'permission':False})
	else:
		redirect('/taskManager/', {'logged_in':False})

def newtask(request, project_id):

	if request.method == 'POST':
	   
		proj = Project.objects.get(pk = project_id)

		task_text = request.POST.get('task_text', False)
		task_title = request.POST.get('task_title', False)
		now = datetime.datetime.now()
	   
		task = Task(
		task_text = task_text,
		title = task_title,
		pub_date = now,
		assoc_project = proj)

		task.save()
		task.users_assigned = [request.user]

		return redirect('/taskManager/' + project_id + '/', {'new_task_added':True})
	else:
		return render_to_response('taskManager/createTask.html', {'proj_id':project_id}, RequestContext(request))

def newproj(request):

	if request.method == 'POST':
	   
		project_title = request.POST.get('project_title', False)
		project_text = request.POST.get('project_text', False)
		now = datetime.datetime.now()
	   
		project = Project(project_title = project_title,
		project_text = project_text,
		start_date = now)
		project.save()
		project.users_assigned = [request.user]
		
		return redirect('/taskManager/', {'new_project_added':True})
	else:
		return render_to_response('taskManager/createProject.html', {}, RequestContext(request))

def logout_view(request):
	logout(request)
	latest_Project_list = Project.objects.order_by('-start_date')
	return render(request, 'taskManager/index.html', {'latest_Project_list': latest_Project_list})

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username', False)
		password = request.POST.get('password', False)

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				# Redirect to a success page.
				return redirect('/taskManager/')
			else:
				# Return a 'disabled account' error message
				return redirect('/taskManager/', {'disabled_user':True})
		else:
			# Return an 'invalid login' error message.
			return render(request, 'taskManager/login.html', {'failed_login': False})
	else:
			# Return an 'invalid login' error message.
			return render_to_response('taskManager/login.html', {}, RequestContext(request))

def register(request):

	context = RequestContext(request)

	registered = False

	if request.method == 'POST':

		user_form = UserForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			user.set_password(user.password)

			#add user to lowest permission group
			#grp = Group.objects.get(name='team_member')
			#user.groups.add(grp)

			user.save()

			# Update our variable to tell the template registration was successful.
			registered = True
		
		#else:
		 #   print user_form.errors

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()

	# Render the template depending on the context.
	return render_to_response(
			'taskManager/register.html',
			{'user_form': user_form, 'registered': registered},
			context)

def index(request):
	latest_Project_list = Project.objects.order_by('-start_date')
	
	admin_level = False

	if request.user.groups.filter(name='admin_g').exists():
		admin_level = True

	list_to_show = []
	for project in latest_Project_list:
		if(project.users_assigned.filter(username= request.user.username)).exists():
			list_to_show.append(project)

	if request.user.is_authenticated():
		  return redirect("/taskManager/dashboard")
	else:
		return render(
			request, 
			'taskManager/index.html', 
			{'latest_Project_list': latest_Project_list, 
			'user':request.user , 
			'admin_level':admin_level }
			)	

def proj_details(request, project_id):
	proj = Project.objects.filter(users_assigned = request.user.id, pk = project_id)
	if not proj:
	  messages.warning(request, 'You are not authorized to view this project')
	  return redirect('/taskManager/dashboard')
	else:
	  proj = Project.objects.get(pk=project_id)

	  return render(request, 'taskManager/proj_details.html', {'proj':proj})

def task_details(request, project_id, task_id):

	task = Task.objects.get(pk = task_id)

	logged_in = True

	if not request.user.is_authenticated():
		logged_in =False

	admin_level = False
	if request.user.groups.filter(name='admin_g').exists():
		admin_level = True

	pmanager_level = False
	if request.user.groups.filter(name='project_managers').exists():
		pmanager_level = True

	assigned_to = False
	if task.users_assigned.filter(username= request.user.username).exists():
		assigned_to = True
	elif admin_level == True:
		assigned_to = True
	elif pmanager_level == True and proj.users_assigned.filter(username= request.user.username).exists():
		assigned_to = True


	if request.method == 'POST':
		
		notes_input = request.POST.get('comment', False)
		image_url = request.POST.get('image', False)

		newNote = Notes()
		#if notes_input != "" and image_url != "":
		newNote = Notes(note_text = notes_input, image_url = image_url, task = task, user = request.user.username)

		newNote.save()


	return render(request, 'taskManager/task_details.html', {'task':task, 'assigned_to':assigned_to, 'logged_in':logged_in, 'completed_task': "Yes" if task.completed else "No"})

def dashboard(request):
	latest_Project_list = Project.objects.order_by('-start_date')
	return render(request, 'taskManager/dashboard.html',  {'latest_Project_list': latest_Project_list, 'user':request.user })
	
def tutorials(request):
	return render(request, 'taskManager/tutorials.html', {'user':request.user})
	
def show_tutorial(request, vuln_id):
	if vuln_id in ["injection", "brokenauth", "xss", "idor", "misconfig", "exposure", "access", "csrf"< "components", "redirects"]:
		return render(request, 'taskManager/tutorials/' + vuln_id+'.html')
	else:
		return render(request, 'taskManager/tutorials.html', {'user':request.user});

def profile(request):
	return HttpResponse('..')