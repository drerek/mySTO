from django.conf.urls import url, include

from loginsys.views import success, RegisterFormView, login, logout

urlpatterns = [
        url(r'^register/', RegisterFormView.as_view()),
        url(r'^success/', success),
        url(r'^accounts/login/$',  login),
        url(r'^accounts/logout/$', logout),
          ]