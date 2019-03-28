from django.shortcuts import render
from client.models import Client
from .forms import New_Client_Form
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def client(request):
    clients = Client.objects.all()
    context = {
        'client_data': clients,
    }
    return render(request, "client/client.html", context)


def add_new_client(request):
    if request.method == 'POST':
        form = New_Client_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client Added!')
            return HttpResponseRedirect('/client')

    form = New_Client_Form()
    context = {
        'form': form,
        'origin': 'Client'
    }
    return render(request, 'client/add_new_client.html', context)

