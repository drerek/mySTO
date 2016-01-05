# -- coding: utf-8 --
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
from app.models import Details


def home(request):
    username = auth.get_user(request).username
    if username:
        return render_to_response('home.html', {'username' : auth.get_user(request).username, 'first_name':auth.get_user(request).first_name}, context_instance = RequestContext(request))
    else:
        return render_to_response('home.html', {'username' : auth.get_user(request).username}, context_instance = RequestContext(request))

def tabl(request):
    username = auth.get_user(request).username
    if username:
        return render_to_response('tableall.html', {'detail': Details.objects.all(), 'username' : auth.get_user(request).username, 'first_name':auth.get_user(request).first_name}, context_instance = RequestContext(request))
    else:
        return render_to_response('tableall.html', {'detail': Details.objects.all(), 'username' : auth.get_user(request).username}, context_instance = RequestContext(request))

def about(request):
    username = auth.get_user(request).username
    if username:
        return render_to_response('about.html', {'username' : auth.get_user(request).username, 'first_name':auth.get_user(request).first_name}, context_instance = RequestContext(request))
    else:
        return render_to_response('about.html', {'username' : auth.get_user(request).username}, context_instance = RequestContext(request))


def tableforeach(request, cars_id=1):
    username = auth.get_user(request).username
    if username:
        return render_to_response('tableall.html', {'detail' : Details.objects.filter(details_cars_id=cars_id), 'cars_id':cars_id, 'username' : auth.get_user(request).username,
                         'first_name': auth.get_user(request).first_name}, context_instance = RequestContext(request))
    else:
        return render_to_response('tableall.html', {'detail' : Details.objects.filter(details_cars_id=cars_id), 'cars_id':cars_id, 'username' : auth.get_user(request).username}, context_instance = RequestContext(request))