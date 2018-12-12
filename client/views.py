from django.shortcuts import render
from client.models import Client


def client(request):
    return render(request, "client/client.html")
