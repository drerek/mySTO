from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template


# Create your views here.
from app.models import Cars, Details


def home(request):
    t = get_template('home.html')
    html = t.render()
    return HttpResponse(html)

def tabl(request):
    t = get_template('tabl.html')
    html = t.render(Context({'detail' : Details.objects.all()}))
    return HttpResponse(html)

def about(request):
    t = get_template('about.html')
    html = t.render()
    return HttpResponse(html)
