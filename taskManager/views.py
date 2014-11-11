import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.views.generic import RedirectView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, Permission, User
from taskManager.forms import UserForm, GroupForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from taskManager.models import Task, Project #,CommentForm

#20821e4abaea95268880f020c9f6768288f3725a


def manageGroups(request):

    user  = request.user

    if user.is_authenticated():
        logged_in = True

        if user.has_perm('can_change_group'):
			
            user_list = User.objects.order_by('date_joined')

            if request.method == 'POST':
                x=1

            else:	
                group_form = GroupForm()
                return render_to_response('taskManager/manage_groups.html', 
				    {'group_form':group_form,'users':user_list, 'logged_in':logged_in}, RequestContext(request))
        else:
            return redirect('/taskManager/', {'permission':False})
    else:
        redirect('/taskManager/', {'logged_in':False})

def newtask(request, project_id):

    if request.method == 'POST':
       
        proj = Project.objects.get(pk = project_id)

        task_text = request.POST.get('task_text', False)
        now = datetime.datetime.now()
       
        task = Task(
        task_text = task_text,
        pub_date = now,
        assoc_project = proj)
        
        task.save()

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

        return redirect('/taskManager/', {'new_project_added':True})
    else:
        return render_to_response('taskManager/createProject.html', {}, RequestContext(request))

def logout_view(request):
    logout(request)
    latest_Project_list = Project.objects.order_by('-start_date')
    return render(request, 'taskManager/index.html', {'latest_Project_list': latest_Project_list})
    # Redirect to a success page.

def login_view(request):

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
            grp = Group.objects.get(name='team_member')
            user.groups.add(grp)

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

	if request.user.has_perm('can_change_group'):
		admin_level = True

	return render(request, 'taskManager/index.html',
    {'latest_Project_list': latest_Project_list, 'user':request.user , 'admin_level':admin_level })

def proj_details(request, project_id):

    proj = Project.objects.get(pk = project_id)
    logged_in = True

    if not request.user.is_authenticated():
        logged_in =False
	
    return render(request, 'taskManager/proj_details.html', {'proj':proj, 'logged_in':logged_in})

def the_comments(request, task_id):
	response = "You're looking at the comments of question %s."
	return HttpResponse(response % task_id)

def detail(request, task_id, project_id):
    task = Task.objects.get(pk = task_id)
    logged_in = True

    if not request.user.is_authenticated():
        logged_in =False

    return render(request, 'taskManager/detail.html', {'task':task, 'logged_in':logged_in})

def thanks(request):
	response = "We are grateful for your comment!"
	return HttpResponse(response)
