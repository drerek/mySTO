from django.db import models
# -- coding: utf-8 --

# Create your models here.
class Cars(models.Model):
    class Meta():
        db_table = 'cars'

    cars_name = models.CharField(max_length=200)
    cars_model = models.CharField(max_length=200)

    def __str__(self):
        return self.cars_name + " " + self.cars_model


class Details(models.Model):
    class Meta():
        db_table = 'details'

    details_name = models.CharField(max_length=200)
    details_price = models.IntegerField()
    details_isav = models.BooleanField(default=False)
    details_cars = models.ForeignKey(Cars)

    def __str__(self):
        return self.details_name.encode('utf-8')

