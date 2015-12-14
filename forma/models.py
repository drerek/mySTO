from django.contrib.auth.models import User
from django.db import models
from app.models import Cars, Details


class Forma(models.Model):
    class Meta():
        db_table = 'forma'

    user_name = models.ForeignKey(User)
    first_name = models.CharField(max_length=200, verbose_name="Ім'я замовника")
    last_name = models.CharField(max_length=200, verbose_name="Призвіще замовника")
    car_name = models.ForeignKey(Cars, verbose_name="Виберіть автомобіль")
    detail = models.ForeignKey(Details, verbose_name="Виберіть деталь")
    problem = models.TextField(max_length=200, default='', verbose_name="Побажання")
    date = models.DateTimeField(verbose_name="Забронюйте дату")
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M")
