from django.shortcuts import render
from django.views.generic import CreateView
from client.models import Client
from order.models import Order
from lib.key_generator import key_generator
from .forms import Invoice, Pre_Invoice


def invoice(request):
    client = Client.objects.all()
    order = Order.objects.all()
    client_name = client.values("Client_Name")
    client_id = client.values("Client_Id")
    order_id = order.values("Order_Id")
    client_key = key_generator("Client")
    order_key = key_generator("Order")

    context = {
        'client_data': client,
        'order_id': order_id,
        'client_key': client_key,
        'order_key': order_key
    }
    return render(request, 'invoice/invoice.html', context)


def generate_invoice(request):
    if request.method == 'POST':
        form = Invoice(request.POST)
        if form.is_valid():
            form.save()

    form = Invoice()
    return render(request, 'invoice/generate_invoice.html', {'form': form})


def generate(request):
    if request.method == 'POST':
        Invoice_Client = request.POST.get("Invoice_Client")
        Invoice_Order = request.POST.get("Invoice_Order")
        print(Invoice_Client, Invoice_Order)
        client = Client.objects.get(pk=Invoice_Client)
        context = {
            'invoice_client_id': client.Client_Id,
            'invoice_client_name': client.Client_Name,
            'invoice_order': Invoice_Order
        }

    return render(request, 'invoice/generate_invoice.html', context)
