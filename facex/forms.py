from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from users_app.models import UserProfile

from .models import Department, FieldOfStudy, School, SchoolProgram, Student

department_choice = Department.objects.all()
fieldofstudy_choice = FieldOfStudy.objects.all()
school_program_choice = SchoolProgram.objects.all()
school_choice = School.objects.all()

User = get_user_model()

class UserPro(UserCreationForm):
	class Meta:
		model = User
		fields = ('first_name','middle_name','phone','last_name','email','password1','password2','date_of_birth','region')


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('school_program','field_of_study','school','department','image','id_n','sex','cafe_status','year_of_study')
		'''
		widgets = {
			'field_of_study' : forms.Select(choices = 'fieldofstudy_choice'),
			'dept' : forms.Select(choices = 'department_choice'),
			'school_choice' : forms.Select(choices = 'school_choice'),
			'school_program_choice' : forms.Select(choices = 'school_program_choice'),

		}
'''