from django.db import models
from facex.models import Student

from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
	user = models.OneToOneField(Student, on_delete = models.CASCADE, null = True, blank=True)
	middle_name = models.CharField(max_length = 150, null = True, blank= True)
	phone = models.CharField(max_length = 10, null = True, blank =True)
	profile_picture = models.ImageField(upload_to = 'profile_picture/%y%m%d')

	def __str__(self):
		return self.username

