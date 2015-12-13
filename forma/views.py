from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib import auth
from django.views.generic import FormView

from forma.forms import CreateForma
from forma.models import Forma
# Create your views here.

class FormaView(FormView):

    form_class = CreateForma

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/success/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "forma.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        #form.user_name = self.get_form_kwargs
        form.save()

        # Вызываем метод базового класса
        return super(FormaView, self).form_valid(form)