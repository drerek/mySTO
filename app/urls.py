from django.conf.urls import url

from app.views import home, tabl, about, tableforeach

urlpatterns = [
    url(r'^table/all/$', tabl),
    url(r'^table/get/(?P<cars_id>\d+)$', tableforeach),
    url(r'^about/', about),
    url(r'^', home),
    ]
