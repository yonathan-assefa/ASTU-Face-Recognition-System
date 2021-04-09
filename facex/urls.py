from django.urls import path
from .views import *

urlpatterns = [

	path('index/',index, name='index'),
	path('register/',register_user, name='register'),
	path('logs/',log_list_view, name='logs')
]

