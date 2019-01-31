from django.shortcuts import render
from client.models import Client


def invoice(request):
    client = Client.objects.all()
    client_name = client.values("Client_Name")
    client_id = client.values("Client_Id")
    context = {
        'client_name': client_name,
        'client_id': client_id
    }
    return render(request, 'invoice/invoice.html', context)

