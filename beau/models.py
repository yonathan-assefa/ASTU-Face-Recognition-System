from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Continent(models.Model):
    name = models.CharField(max_length=255)

class Country(models.Model):
    continent = models.ForeignKey(Continent, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)




class Location(models.Model):
    continent = models.ForeignKey(Continent,on_delete = models.CASCADE)
    country = ChainedForeignKey(
        Country,
        chained_field="continent",
        chained_model_field="continent",
        show_all=False,
        auto_choose=True,
        sort=True)
   # area = models.ForeignKey(Area)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)