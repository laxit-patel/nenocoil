from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client, name="clients"),
    url(r'^add_new_client$',views.add_new_client, name="add_new_clients")
]
