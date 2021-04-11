from datetime import date

from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

from users_app.models import UserProfile

cafe_choice = [
	('C','Cafe'),
	('NC','None Cafe')
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

	def __str__(self):
		return self.id_n



class StudentLog(models.Model):
	log_history = models.FileField(upload_to = 'media/logs/%y/%m')
	log_date = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.log_date.__str__()
