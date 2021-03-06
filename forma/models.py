# -- coding: utf-8 --
from django.contrib.auth.models import User
from django.db import models
import datetime
from app.models import Cars, Details


class Forma(models.Model):
    class Meta():
        db_table = 'forma'

    user_name = models.ForeignKey(User)
    first_name = models.CharField(max_length=200, verbose_name="Ім'я замовника")
    last_name = models.CharField(max_length=200, verbose_name="Призвіще замовника")
    car_name = models.ForeignKey(Cars, verbose_name="Виберіть автомобіль")
    problem = models.TextField(max_length=200, default='', verbose_name="Побажання")
    date = models.DateField(verbose_name="Забронюйте дату")
    time = models.TimeField(verbose_name="Забронюйте час")
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        #dt=self.date.strftime("%Y-%m-%d")
        #return self.date.strftime("%Y-%m-%d")+" "+self.time.strftime("%H:%M")
        return self.date.strftime("%Y-%m-%d")+self.time.strftime(" %H:%M")
