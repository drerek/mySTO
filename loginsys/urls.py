from django.conf.urls import url, include

from loginsys.views import RegisterFormView

urlpatterns = [
          url(r'^register/', RegisterFormView.as_view()),
          ]