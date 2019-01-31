from django.conf.urls import url, include
from django.urls import path
from . import views
from .views import dashboard


urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^dashboard/', include('dashboard.urls'), name='dashboard'),
]
