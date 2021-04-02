from django.db import models
from facex.models import Student

from django.contrib.auth.models import AbstractUser

region_choice = [
	('AA', 'Addis Ababa'),
	('AF','Afar'),
	('AM','Amhara'),
	('BN','Benishangul-Gumuz'),
	('DD','Dire Dawa'),
	('GM','Gambela'),
	('HR','Harari'),
	('Or','Oromiya'),
	('SD','Sidama'),
	('SNNP','Southern Nations, Nationalities, and Peoples'),
	('TG','Tigray'),
]


sex_choice = [
	('M','Male'),
	('F','Female'),

]


class UserProfile(AbstractUser):
	user = models.OneToOneField(Student, on_delete = models.PROTECT, null = True, blank=True)
	phone = models.CharField(max_length = 10, null = True, blank =True)
	sex = models.CharField(max_length = 1 , choices = sex_choice, null = True, blank = True)
	profile_picture = models.ImageField(upload_to = 'media/profile_picture/%y%m%d')
	email = models.EmailField(null = True, blank =True)
	date_of_birth = models.DateField(null = True, blank =True)
	region = models.CharField(max_length = 4, choices = region_choice, null = True, blank =True)

