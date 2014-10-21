from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from taskManager.forms import UserForm

from taskManager.models import Task, CommentForm, Project

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
	latest_Project_list = Project.objects.order_by('-start_date')[:5]
	#template = loader.get_template('taskManager/index.html')
	#context = RequestContext(request, {
	#	'latest_task_list': latest_task_list,
	#})
	#return HttpResponse(template.render(context))
	return render(request, 'taskManager/index.html', {'latest_Project_list': latest_Project_list})

#def detail(request, task_id):
#	return HttpResponse("You're looking at question %s" % task_id)


def login(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('login.html',{'state':state, 'username': username})


def proj_details(request, project_id):
	proj = Project.objects.get(pk = project_id)
	return render(request, 'taskManager/proj_details.html', {'proj':proj})


def the_comments(request, task_id):
	response = "You're looking at the comments of question %s."
	return HttpResponse(response % task_id)

def detail(request, task_id, foreign_key):
	#try:
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
		else:
			form = CommentForm()

	task = Task.objects.get(pk = task_id)
	#except Task.DoesNotExist:
	#	raise Http404
	return render(request, 'taskManager/detail.html', {'task':task})

def thanks(request):
	response = "We are grateful for your comment!"
	return HttpResponse(response)

# Create your views here.
