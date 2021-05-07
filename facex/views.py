from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import StudentForm, UserPro
from users_app.models import UserProfile

from django.http import HttpResponse

def my_home(request):
	return render(request, 'index.html', {})


def my_home2(request):
	return render(request, 'index2.html', {})

def my_home3(request):
	return render(request, 'index3.html', {})

def base(request):
	return render(request, 'base.html', {})

def login(request):
	return render(request, 'login.html', {})

def form_view(request):
	return render(request, 'form.html', {})

def index(request):
	return render(request,'home.html', context ={'text':'Hello World'})

def iv(request):
	return HttpResponse('<h2>favicon.ico</h2>')


def setter(form2,profile_form,form1,temp):
	passwd = form2.cleaned_data['password1']
	print(passwd)
	profile_form.set_password(passwd)
	#profile_form.id = form2.cleaned_data['id']
	profile_form.username = form1.cleaned_data['id_n']
	profile_form.first_name = form2.cleaned_data['first_name']
	profile_form.last_name = form2.cleaned_data['last_name']
	profile_form.phone = form2.cleaned_data['phone']
	profile_form.user = temp
	profile_form.profile_picture = form1.cleaned_data['image']
	profile_form.middle_name = form2.cleaned_data['middle_name']
	#form2.profile_picture = form1.cleaned_data['image']
	profile_form.email = form1.cleaned_data['email']
	return profile_form

def register_user(request):
	if request.method == 'POST':
		form1 = StudentForm(request.POST, request.FILES)
		form2 = UserPro(request.POST)
		if form1.is_valid() and form2.is_valid():
			profile_form = UserProfile()
			temp = form1.save(commit = False)
			profile_form = setter(form2,profile_form,form1,temp)
			form1.save(commit = True)
			profile_form.save()
			print("Successfully wiped")
			return redirect('facex:register')
		else:
			print('not Successfully reged')			
			
	else:
		form2 = UserPro()
		form1 = StudentForm()

	context = {'form1':form1,'form2':form2}
	return render(request, 'student_management/register.html',context)