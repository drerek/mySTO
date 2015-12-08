from django.conf.urls import url, include

from app.views import home, tabl, about

urlpatterns = [
    url(r'^home/', home),
    url(r'^table/all/$', tabl),
    url(r'^table/get/(?<cars_id>)\d+$', tableforeach),
    url(r'^about/', about),
            ]
