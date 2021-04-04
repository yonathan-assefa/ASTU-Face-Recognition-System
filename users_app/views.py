from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
#from .forms import ProfileForm
#from facex.models import Student 

from django.http import HttpResponse

User = get_user_model()


def home(request):
	return HttpResponse('<b>Hello World</b>')


