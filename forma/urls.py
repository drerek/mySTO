from django.views.generic import FormView

from app.views import home
from forma.views import FormaView
from django.conf.urls import url, include

urlpatterns = [
 url(r'^form/', FormaView.as_view()),
]