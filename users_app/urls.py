from django.urls import path

from . import views

urlpatterns = [
	path('home/',views.home, name = 'home'),
    path('login/',views.login_user,  name = 'login'),
    path('logout/',views.logout_user, name = 'logout'),
   	#path('edit_profile/',views.edit_profile,name='edit_profile'),
    #path('edit_profile',views.EditProfileView.as_view(),name='edit_profile'),
    path('edit_profile/', views.EditProfileView.as_view(), name="edit_profile"),
    path('change_password/',views.change_password,name='change_password'),
]