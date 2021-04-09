from django import forms
from .models import Student, Department, FieldOfStudy , SchoolProgram, School
from django.contrib.auth import get_user_model
from users_app.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


department_choice = Department.objects.all()
fieldofstudy_choice = FieldOfStudy.objects.all()
school_program_choice = SchoolProgram.objects.all()
school_choice = School.objects.all()

User = get_user_model()

class UserPro(UserCreationForm):
	middle_name = forms.CharField(widget =forms.TextInput(
								attrs = {'placeholder':'Middle Name'}),)
	phone = forms.CharField(widget =forms.TextInput(
								attrs = {'placeholder':'Phone'}),max_length = 10)
	class Meta:
		model = User
		fields = ('first_name','last_name','password1','password2')


class StudentForm(forms.ModelForm):
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email','Label':'Email'}))
	class Meta:
		model = Student
		fields = ('school_program','field_of_study','school','department','image','id_n','sex','cafe_status','year_of_study','date_of_birth','region')
		'''
		widgets = {
			'field_of_study' : forms.Select(choices = 'fieldofstudy_choice'),
			'dept' : forms.Select(choices = 'department_choice'),
			'school_choice' : forms.Select(choices = 'school_choice'),
			'school_program_choice' : forms.Select(choices = 'school_program_choice'),

		}
'''