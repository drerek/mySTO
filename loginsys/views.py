# -- coding: utf-8 --
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
# Create your views here.
from django.template import RequestContext
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from loginsys.forms import UserCreateForm


class RegisterFormView(FormView):
    form_class = UserCreateForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/accounts/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

def success(request):
    return HttpResponseRedirect("/accounts/login/")

def login(request):
    if auth.get_user(request).username:
        return HttpResponseRedirect("/home/")
    else:
        args = {}
        args['username'] = auth.get_user(request).username
        args.update(csrf(request))
        if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Правильный пароль и пользователь "активен"
                auth.login(request, user)
                # Перенаправление на "правильную" страницу
                return HttpResponseRedirect("/home/")
            else:
                #Отображение страницы с ошибкой
                args['login_error'] = "Такого користувача не знайдено :("

                return render_to_response('login.html', args, context_instance = RequestContext(request))
        else:
            return render_to_response('login.html', args, context_instance = RequestContext(request))



def logout(request):
    if auth.get_user(request).username:
        auth.logout(request)
        return redirect('/home/')
    else:
        t = get_template('errors.html')
        html = t.render()
        return HttpResponse(html)



