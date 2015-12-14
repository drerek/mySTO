from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.template.loader import get_template

from forma.forms import CreateForma
from forma.models import Forma


def add_forma(request):
    if request.method == 'POST':
         form = CreateForma(request.POST)
         if form.is_valid():
             forma = form.save(commit=False)
             forma.user_name = request.user
             forma.save()
             return HttpResponseRedirect("/home/")
    else:
        form = CreateForma()
        return render(request, 'forma.html', {'form': form, 'username':auth.get_user(request).username})

def myforms(request):
    t = get_template('myforms.html')
    html = t.render({'myforms' : Forma.objects.filter(user_name=auth.get_user(request)), 'username' : auth.get_user(request).username})
    return HttpResponse(html)