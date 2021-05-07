from django import forms
from .models import Student, Department, FieldOfStudy , YearOfStudy
from django.contrib.auth import get_user_model
from users_app.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


department_choice = Department.objects.all()
fieldofstudy_choice = FieldOfStudy.objects.all()
yearofstudy_choice = YearOfStudy.objects.all()

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

	class Meta:
		model = Student
		fields = ('image','id_n','sex','email',
				  'date_of_birth','region','cafe_status',
				  'year_of_study','field_of_study','dept',)
		widgets = {
			'year_of_study' : forms.Select(choices = yearofstudy_choice, 
										   attrs= {'class':'form-control'}),
			'field_of_study' : forms.Select(choices = 'fieldofstudy_choice'),
			'dept' : forms.Select(choices = 'department_choice'),

		}
