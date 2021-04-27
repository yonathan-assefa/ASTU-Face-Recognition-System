from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (PasswordChangeForm, UserChangeForm,
                                       UserCreationForm)
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import EditProfileForm
from .models import UserProfile

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)


#from .forms import ProfileForm
#from facex.models import Student 



User = get_user_model()


user_profile = None

@login_required
def home(request):
	context = {'user_profile':user_profile}
	return render(request, 'student_management/home.html')



def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password=password)
		if user is not None:
			login(request,user)
			messages.success(request,('You have been logged in'))
			return redirect("home")
		else:
			messages.success(request,('Try agian'))
			return redirect("login")
	else:
		return render(request,'student_management/login.html',{})

@login_required
def logout_user(request):
	logout(request)
	messages.success(request,("You have been logout"))
	return redirect('home')

# @login_required
# def edit_profile(request):
# 	if request.method == "POST":
# 		form = EditProfileForm(request.POST ,request.FILES,instance =request.user)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request,("Profile Updated successfully"))
# 			return redirect('home')

# 	else:
# 		form = EditProfileForm(instance=request.user)

# 	context = {'form':form}

# 	return render(request,'student_management/edit_profile.html',context)

@login_required
def change_password(request):
	if request.method == "POST":
		form = PasswordChangeForm(data=request.POST, user =request.user)
		if form.is_valid():
			form.save()
			#update_session_auth_hash(request,form.user)
			messages.success(request,("Password Updated successfully"))
			return redirect('home')

	else:
		form = PasswordChangeForm(user=request.user)

	context = {'form':form}

	return render(request,'student_management/change_password.html',context)


class EditProfileView(LoginRequiredMixin,UpdateView):
	model = UserProfile
	form_class = EditProfileForm
	template_name = 'student_management/edit_profile.html'

	def get_object(self, *args, **kwargs):
		user = get_object_or_404(User, pk=self.request.user.pk)
		return user

	def get_success_url(self, *args, **kwargs):
		return reverse_lazy("home")

