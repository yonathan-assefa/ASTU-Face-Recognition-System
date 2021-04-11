from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [

	path('index/',TemplateView.as_view(template_name='student_management/home.html'), name='index'),
	#path('register/',register_user, name='register'),
	#path('logs/',log_list_view, name='logs'),
	path('sign/', SignUpView.as_view(), name='sign'),
]

