# -- coding: utf-8 --
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext
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
        return render_to_response('forma.html', {'form': form, 'username':auth.get_user(request).username},context_instance = RequestContext(request))

def myforms(request):
    t = get_template('myforms.html')
    html = t.render({'myforms' : Forma.objects.filter(user_name=auth.get_user(request)), 'username' : auth.get_user(request).username})
    return HttpResponse(html)