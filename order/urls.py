from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.order, name="order"),
    url(r'^add_new_order', views.add_new_order, name='add_new_order')
]
