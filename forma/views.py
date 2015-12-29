# -- coding: utf-8 --
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template

from app.models import Details
from forma.forms import CreateForma
from forma.models import Forma
import calendar

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
        username=auth.get_user(request).username
        zanyato = Forma.objects.all()
        time_list=[]
        for zanyat in zanyato:
            time_list.append(zanyat)
        if username:
            return render_to_response('forma.html', {'timelist':time_list, 'zanyato':zanyato, 'form': form,'first_name':auth.get_user(request).first_name, 'username':auth.get_user(request).username},context_instance = RequestContext(request))
        else:
            return render_to_response('forma.html', {'zanyato':zanyato,'timelist':time_list, 'form': form, 'username':auth.get_user(request).username},context_instance = RequestContext(request))


def myforms(request):
    t = get_template('myforms.html')
    username=auth.get_user(request).username
    if username:
        html = t.render({'myforms' : Forma.objects.filter(user_name=auth.get_user(request)),'first_name':auth.get_user(request).first_name, 'username' : auth.get_user(request).username})
    else:
        html = t.render({'myforms' : Forma.objects.filter(user_name=auth.get_user(request)), 'username' : auth.get_user(request).username})
    return HttpResponse(html)


def date_from_ajax (request):
    if request.method == "GET" and request.is_ajax():
        time=Forma.objects.filter(date=request.GET["data"])
        time_list=[]
        for times in time:
            time_list.append(times.time.strftime("%H"))
        return JsonResponse({'time_list':time_list})