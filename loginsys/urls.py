from django.conf.urls import url, include

from loginsys.views import success, RegisterFormView, login, logout

urlpatterns = [
        url(r'^register/', RegisterFormView.as_view()),
        url(r'^accounts/login/$',  login),
        url(r'^accounts/logout/$', logout),
        url(r'^ulogin/', include('django_ulogin.urls')),
          ]