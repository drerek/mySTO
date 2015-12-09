from django.conf.urls import url, include

from loginsys.views import success, RegisterFormView

urlpatterns = [
        url(r'^register/', RegisterFormView.as_view()),
        url(r'^success/', success),
          ]