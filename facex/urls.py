from django.urls import path
from .views import *

urlpatterns = [

	path('index/',index, name='index'),
	path('register/',register_user, name='register'),
]

