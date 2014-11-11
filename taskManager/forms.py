from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import Permission, Group

#from taskManager import Comments


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
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


# class CommentForm(forms.Form):
# 	the_comment = forms.CharField(widget = forms.Textarea)

# 	class Meta:
# 		model = Comments
# 		fields = ('text')
