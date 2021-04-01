from django.shortcuts import render


def index(request):
	return render(request,'index.html', context ={'text':'Hello World'})