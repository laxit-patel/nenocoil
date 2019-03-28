from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.design, name="design"),
    url(r'^add_new_design$', views.add_new_design, name="add_new_design"),
    url(r'^add_new_drawing$', views.add_new_drawing, name="add_new_drawing"),
]
