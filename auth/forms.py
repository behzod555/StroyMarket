from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from store.models import *
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields=['username', 'email']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phonenumber']
        