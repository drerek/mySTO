# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forma', '0002_auto_20151212_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='forma',
            name='problem',
            field=models.CharField(default='', max_length=200),
        ),
    ]
