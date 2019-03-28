from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.product, name="product"),
    url(r'^add_new_product$', views.add_new_product, name="add_new_product"),
    url(r'^add_new_design$', views.add_new_design, name='add_new_design'),
    url(r'^add_new_producttype$', views.add_new_producttype, name='add_new_producttype'),
]
