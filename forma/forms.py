from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.db.transaction import commit
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.core.context_processors import csrf
from django.template import RequestContext

from forma.models import Forma
from django.contrib import auth

class CreateForma(forms.ModelForm):

    class Meta:
            model = Forma
            fields = ["user_name", "first_name", "last_name", "car_name", "detail", "problem", "date"]

    def save(self, commit=True):
            forma = super(CreateForma, self).save(commit=False)
            #forma.username = 'auth.User'
            #forma.first_name = self.cleaned_data["first_name"]
            #forma.user_name = User.objects.get(self.user)
            #forma.user_name=auth.get_user
            #forma.user_name_id = self.user

            if commit:
                forma.save()
            return forma