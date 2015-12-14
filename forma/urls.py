from django.views.generic import FormView

from app.views import home
from forma.views import add_forma
from django.conf.urls import url, include

urlpatterns = [
 url(r'^form/', add_forma),
]