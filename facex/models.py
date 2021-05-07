from django.db import models



from django.db import models


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
	image = models.ImageField(upload_to = 'images/face_datas',unique = True)
	id_n = models.CharField(max_length = 12,unique = True)
	sex = models.CharField(max_length = 1 , choices = sex_choice)

	cafe_status = models.CharField(max_length = 2, choices = cafe_choice)

	dept = models.ForeignKey(Department, on_delete = models.PROTECT)
	field_of_study = models.ForeignKey(FieldOfStudy, on_delete = models.PROTECT)
	year_of_study = models.ForeignKey(YearOfStudy, on_delete = models.PROTECT)
	email = models.EmailField(null = True, blank =True)
	date_of_birth = models.DateField()
	region = models.CharField(max_length = 4, choices = region_choice)


	def __str__(self):
		return self.id_n



