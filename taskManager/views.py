from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.views.generic import RedirectView
from django.contrib.auth import authenticate, login
from taskManager.forms import UserForm

from taskManager.models import Task, CommentForm, Project

#20821e4abaea95268880f020c9f6768288f3725a

from django.contrib.auth import logout

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
                return redirect('/taskManager/')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'taskManager/login.html', {'failed_login': False})
            #return render_to_response('taskManager/login.html', {'failed_login': failed_login}, RequestContext(request))
    else:
            # Return an 'invalid login' error message.
            return render_to_response('taskManager/login.html', {}, RequestContext(request))


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            user.set_password(user.password)
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
	#template = loader.get_template('taskManager/index.html')
	#context = RequestContext(request, {
	#	'latest_task_list': latest_task_list,
	#})
	#return HttpResponse(template.render(context))
	return render(request, 'taskManager/index.html', {'latest_Project_list': latest_Project_list})

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

# Create your views here.
