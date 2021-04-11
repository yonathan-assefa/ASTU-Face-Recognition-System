from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

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



class UserProfile(AbstractUser):
	username_validator = RegexValidator(r'^[\w.@+-/]+\Z',message = (
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    ))
	username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
	middle_name = models.CharField(max_length = 150, null = True, blank= True)
	phone = models.CharField(max_length = 10, null = True, blank =True)
	profile_picture = models.ImageField(upload_to = 'profile_picture/%y%m%d', blank = True, null = True)
	date_of_birth = models.DateField(blank = True, null = True)
	region = models.CharField(max_length = 4, choices = region_choice, blank = True, null = True)

	def __str__(self):
		return self.username

