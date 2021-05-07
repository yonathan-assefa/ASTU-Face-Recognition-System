from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserProfile
from facex.models import Student

User = get_user_model()

'''
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('image','name','id_n','cafe_status','year_of_study','field_of_study','dept')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('user','sex','phone','email','date_of_birth','region','profile_picture')

'''