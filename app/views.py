from django.contrib import auth
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template


# Create your views here.
from app.models import Cars, Details


def home(request):
    t = get_template('home.html')
    html = t.render({'username' : auth.get_user(request).username})
    return HttpResponse(html)

def tabl(request):
    t = get_template('tableall.html')
    html = t.render({'detail' : Details.objects.all(), 'username' : auth.get_user(request).username})
    return HttpResponse(html)

def about(request):
    t = get_template('about.html')
    html = t.render({'username' : auth.get_user(request)})
    return HttpResponse(html)


def tableforeach(request, cars_id=1):
    t = get_template('tableall.html')
    html = t.render({'detail' : Details.objects.filter(details_cars_id=cars_id), 'username' : auth.get_user(request).username})
    return HttpResponse(html)
