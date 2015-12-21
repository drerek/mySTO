# coding=utf-8
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import BaseUserManager
from django.db import models
# --coding: utf-8 --
# Create your models here.

from django_ulogin.models import ULoginUser
from django_ulogin.signals import assign

def catch_ulogin_signal(*args, **kwargs):
    """
    Обновляет модель пользователя: исправляет username, имя и фамилию на
    полученные от провайдера.

    В реальной жизни следует иметь в виду, что username должен быть уникальным,
    а в социальной сети может быть много "тёзок" и, как следствие,
    возможно нарушение уникальности.

    """
    user=kwargs['user']
    json=kwargs['ulogin_data']

    if kwargs['registered']:
        user.username = json['username']
        user.first_name = json['first_name']
        user.last_name = json['last_name']
        user.email = json['email']
        user.save()


assign.connect(receiver=catch_ulogin_signal,
               sender=ULoginUser,
               dispatch_uid='customize.models')