from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.invoice, name="invoice"),
    url(r'^generate$', views.generate),
    url(r'^add_new_client$', views.add_new_client),
    url(r'^add_new_order', views.add_new_order)
    ]
