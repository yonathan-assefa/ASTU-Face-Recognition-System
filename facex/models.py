from django.db import models



from django.db import models


cafe_choice = [
	('C','Cafe'),
	('NC','None Cafe')
]


class Department(models.Model):
	department = models.CharField(max_length = 200)

	def __str__(self):
		return self.department

class FieldOfStudy(models.Model):
	field_of_study = models.CharField(max_length = 200)

	def __str__(self):
		return self.field_of_study

class YearOfStudy(models.Model):
	year_of_study = models.CharField(max_length = 200)

	def __str__(self):
		return self.year_of_study


class Student(models.Model):
	image = models.ImageField(upload_to = 'images/face_datas')
	name = models.CharField(max_length = 150)
	id_n = models.CharField(max_length = 12)
	
	cafe_status = models.CharField(max_length = 2, choices = cafe_choice)

	dept = models.ForeignKey(Department, on_delete = models.PROTECT)
	field_of_study = models.ForeignKey(FieldOfStudy, on_delete = models.PROTECT)
	year_of_study = models.ForeignKey(YearOfStudy, on_delete = models.PROTECT)



	def __str__(self):
		return self.name



