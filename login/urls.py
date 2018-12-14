from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
]
