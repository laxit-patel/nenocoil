from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'logout^$', views.dashboard, name="logout"),
]
