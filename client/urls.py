from django.conf.urls import url
from django.views.generic import ListView
from client.models import Client

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Client.objects.all(), template_name="client/client.html")),
]
