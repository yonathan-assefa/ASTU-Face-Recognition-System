from django.shortcuts import render,redirect
from .forms import StudentForm, UserPro
from users_app.models import UserProfile
from django.views.generic import ListView,DetailView

from .models import StudentLog, Student

from django.http import HttpResponse


from pathlib import Path 


from django.views.decorators.cache import never_cache

def index(request):
	try:
		current_log = StudentLog()
		current_log.save()
	except:
		pass
	return render(request,'index.html', context ={'text':'Hello World'})

def iv(request):
	return HttpResponse('<h2>favicon.ico</h2>')


def setter(form2,profile_form,form1):
	passwd = form2.cleaned_data['password1']
	profile_form.set_password(passwd)
	#profile_form.id = form2.cleaned_data['id']
	profile_form.username = form1.cleaned_data['id_n']
	profile_form.first_name = form2.cleaned_data['first_name']
	profile_form.last_name = form2.cleaned_data['last_name']
	profile_form.phone = form2.cleaned_data['phone']
	profile_form.profile_picture = form1.cleaned_data['image']
	profile_form.middle_name = form2.cleaned_data['middle_name']
	#form2.profile_picture = form1.cleaned_data['image']
	profile_form.email = form1.cleaned_data['email']
	#profile_form = profile_form.save()
	return profile_form

def stud_setter(form1,profile_form):
	student_form = Student()
	student_form.user_profile = profile_form
	student_form.image = form1.cleaned_data['image']
	student_form.school_program = form1.cleaned_data['school_program']
	student_form.field_of_study = form1.cleaned_data['field_of_study']
	student_form.department = form1.cleaned_data['department']
	student_form.id_n = form1.cleaned_data['id_n']
	student_form.sex = form1.cleaned_data['sex']
	student_form.year_of_study = form1.cleaned_data['year_of_study']
	student_form.cafe_status = form1.cleaned_data['cafe_status']
	student_form.school = form1.cleaned_data['school']
	student_form.date_of_birth = form1.cleaned_data['date_of_birth']
	student_form.region = form1.cleaned_data['region']
	return student_form




@never_cache
def register_user(request):
	if request.method == 'POST':
		form1 = StudentForm(request.POST, request.FILES)
		form2 = UserPro(request.POST)
		if form1.is_valid() and form2.is_valid():
			profile_form = UserProfile()
			profile_form = setter(form2,profile_form,form1)
			student_form = stud_setter(form1,profile_form)
			profile_form.save()
			student_form.save()
			print("Successfully wiped")
			return redirect('register')
		else:
			print('not Successfully reged')			
			
	else:
		form2 = UserPro()
		form1 = StudentForm()

	context = {'form1':form1,'form2':form2}
	return render(request, 'student_management/register.html',context)



fol = Path("./../logs/").rglob('*.lf')



log_files = []
for i in fol:
	ddv=open('./'+str(i))
	pr = ddv.read().split('|')
	to = []
	for i in pr:
		t = i.split('$')
		try:
			to.append(t[0]+' ' + t[1])
		except:
			pass
	log_files.append(to)


print("lof",log_files)

def log_list_view(request):
	return HttpResponse('<h3>Hello papa</h3>')
