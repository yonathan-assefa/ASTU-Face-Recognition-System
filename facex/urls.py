from django.urls import path
from .views import *

app_name = 'facex'

urlpatterns = [
	path('', my_home ,name='my_home'),
	path('base/', base, name='base'),
	path('home2/', my_home2, name='my_home2'),
	path('home3/', my_home3, name='my_home3'),
	path('index/',index, name='index'),
	path('register/',register_user, name='register'),
	path('login/', login, name='login'),
	path('form/', form_view, name='form'),
]

