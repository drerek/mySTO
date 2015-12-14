from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from forma.forms import CreateForma



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
