from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.drawing, name="drawing"),
    url(r'^add_new_drawing$', views.add_new_drawing, name="add_new_drawing"),
    url(r'^add_new_client$', views.add_new_client, name="add_new_client"),
]
