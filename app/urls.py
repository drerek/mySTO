from django.conf.urls import url, include

from app.views import home, tabl, about

urlpatterns = [
    url(r'^home/', home),
    url(r'^table/', tabl),
    url(r'^about/', about),
            ]
