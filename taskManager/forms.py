from django.contrib.auth.models import User
from django import forms

#from taskManager import Comments


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
#look at mass assignments


# class CommentForm(forms.Form):
# 	the_comment = forms.CharField(widget = forms.Textarea)

# 	class Meta:
# 		model = Comments
# 		fields = ('text')
