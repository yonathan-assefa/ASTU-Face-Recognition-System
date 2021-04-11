from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from facex.models import Student

from .models import UserProfile

User = get_user_model()


class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",required = False ,widget = forms.TextInput(attrs = {'type':'hidden',}))
	class Meta:
		model = User
		fields = ('username','email','phone','region','date_of_birth','profile_picture')


