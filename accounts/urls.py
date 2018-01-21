from django.conf.urls import url
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView


urlpatterns = [
    url(r'^registration/', RegisterView.as_view(), name='registration'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
]
