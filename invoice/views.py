from django.shortcuts import render
from client.models import Client
from order.models import Order
from lib.key_generator import key_generator


def invoice(request):
    client = Client.objects.all()
    order = Order.objects.all()
    client_name = client.values("Client_Name")
    client_id = client.values("Client_Id")
    order_id = order.values("Order_Id")
    client_key = key_generator("Client")
    order_key = key_generator("Order")
    context = {
        'client_name': client_name,
        'client_id': client_id,
        'order_id': order_id,
        'client_key': client_key,
        'order_key': order_key
    }
    return render(request, 'invoice/invoice.html', context)

