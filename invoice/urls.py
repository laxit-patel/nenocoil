from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.invoice, name="invoice"),
    url(r'^generate_invoice$', views.generate_invoice),
    url(r'^generate$', views.generate),
    ]
