from django.contrib.auth.models import User
from taskManager.models import Project, Task, Notes
from django import forms
from django.contrib.auth.models import Permission, Group, User


#from taskManager import Comments

def get_my_choices_users():
    # you place some logic here
    user_list = User.objects.order_by('date_joined')
    user_tuple = []
    counter = 1
    for user in user_list:
        user_tuple.append((counter, user))
        counter = counter +1
    return user_tuple


def get_my_choices_tasks(current_proj):
    # you place some logic here
    task_list = []
    tasks = Task.objects.all()
    for task in tasks:
        if task.project == current_proj:
            task_list.append(task)

    task_tuple = []
    counter = 1
    for task in task_list:
        task_tuple.append((counter, task))
        counter = counter +1
    return task_tuple

class ManageTask(forms.Form):
    
    def __init__(self, *args, **kwargs):
        current_project = kwargs.pop('current_proj', None)
        super(ManageTask, self).__init__(*args, **kwargs)
        self.fields['User'] = forms.ChoiceField(
            choices=get_my_choices_users() )
        self.fields['Task'] = forms.ChoiceField(
            choices = get_my_choices_tasks(current_project))


def get_my_choices_projects():
    # you place some logic here
    proj_list = Project.objects.all()
    proj_tuple = []
    counter = 1
    for proj in proj_list:
        proj_tuple.append((counter, proj))
        counter = counter +1
    return proj_tuple

class AssignProject(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(AssignProject, self).__init__(*args, **kwargs)
        self.fields['User'] = forms.ChoiceField(
            choices=get_my_choices_users() )
        self.fields['Project'] = forms.ChoiceField(
            choices = get_my_choices_projects())

#A2: Broken Authentication and Session Management
class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    user_permissions = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	

    class Meta:
    	model = User
    	fields = ('username', 'first_name', 'last_name', 'email', 'password', 'user_permissions')
    #look at mass assignments

_Choices = (
    (1,        'Admin Access'),
    (2,        'Project Manager Access'),
    (3,        'Team Member Access'),
)

class GroupForm(forms.Form):
    question  = forms.ChoiceField(label = 'Permission Level', choices=_Choices, widget=forms.RadioSelect())

    class Meta:
    	model = Group


class AssignemntForm(forms.Form):

    class Meta:
        model = Project
    
class ProjectFileForm(forms.Form):
    name = forms.CharField(max_length=300)
    file = forms.FileField()

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.CharField(max_length=300, required=False)
    picture = forms.FileField(required=False)
