from django.db import models
from django.utils import timezone

from datetime import date

from smart_selects.db_fields import ChainedForeignKey
from users_app.models import UserProfile

cafe_choice = [
	('C','Cafe'),
	('NC','None Cafe')
]

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

YearOfStudy_choice = [
	('FM','Freshman'),
	('SO','Sopomer'),
	('JU','Juniour'),
	('SE','Senior'),
	('GC','GC'),
]

class SchoolProgram(models.Model):
	school_program = models.CharField(max_length = 30)

	def __str__(self):
		return self.school_program


class FieldOfStudy(models.Model):
	school_program = models.ForeignKey(SchoolProgram, on_delete = models.CASCADE)
	field_of_study = models.CharField(max_length = 200)
	def __str__(self):
		return self.field_of_study

class School(models.Model):
	school_program = models.ForeignKey(SchoolProgram, on_delete = models.CASCADE)
	school = models.CharField(max_length = 120)
	field_of_study =  ChainedForeignKey(
        FieldOfStudy,
        chained_field="school_program",
        chained_model_field="school_program",
        show_all=False,
        auto_choose=True,
        sort=True)

	def __str__(self):
		return self.school

class Department(models.Model):
	school_program = models.ForeignKey(SchoolProgram, on_delete = models.CASCADE)
	department = models.CharField(max_length = 200)
	field_of_study =  ChainedForeignKey(
        FieldOfStudy,
        chained_field="school_program",
        chained_model_field="school_program",
        show_all=False,
        auto_choose=True,
        sort=True)
	school =  ChainedForeignKey(
        School,
        chained_field="field_of_study",
        chained_model_field="field_of_study",
        show_all=False,
        auto_choose=True,
        sort=True)

	def __str__(self):
		return self.department



class Student(models.Model):
	school_program = models.ForeignKey(SchoolProgram, on_delete = models.PROTECT)
	user_profile = models.OneToOneField(UserProfile, on_delete = models.CASCADE, unique = True)
	field_of_study =  ChainedForeignKey(
        FieldOfStudy,
        chained_field="school_program",
        chained_model_field="school_program",
        show_all=False,
        auto_choose=True,
        sort=True)
	school =  ChainedForeignKey(
        School,
        chained_field="field_of_study",
        chained_model_field="field_of_study",
        show_all=False,
        auto_choose=True,
        sort=True)	
	department =  ChainedForeignKey(
        Department,
        chained_field="school",
        chained_model_field="school",
        show_all=False,
        auto_choose=True,
        sort=True)

	image = models.ImageField(upload_to = 'images/face_datas',unique = True)
	id_n = models.CharField(max_length = 12,unique = True)
	sex = models.CharField(max_length = 1 , choices = sex_choice)
	cafe_status = models.CharField(max_length = 2, choices = cafe_choice)
	year_of_study = models.CharField(choices = YearOfStudy_choice, max_length = 2)
	date_of_birth = models.DateField()
	region = models.CharField(max_length = 4, choices = region_choice)


	def __str__(self):
		return self.id_n



class StudentLog(models.Model):
	date = models.DateField(default = date.today, unique=True)
	def __str__(self):
		return self.date.__str__()
