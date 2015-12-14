from django.contrib.auth.models import User
from django.db import models
from app.models import Cars, Details


class Forma(models.Model):
    class Meta():
        db_table = 'forma'

    user_name = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car_name = models.ForeignKey(Cars)
    detail = models.ForeignKey(Details)
    problem = models.TextField(max_length=200, default='')
    date = models.DateTimeField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.date