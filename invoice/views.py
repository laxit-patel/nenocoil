from django.shortcuts import render
from django.views.generic import CreateView
from client.models import Client
from order.models import Order
from modules.key_generator import key_generator
from .forms import Invoice, New_Order_Form
from client.forms import New_Client_Form
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


def invoice(request):
    client = Client.objects.all()
    order = Order.objects.all()
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


def generate(request):
    if request.method == 'POST':
        form = Invoice(request.POST)
        invoice_client = request.POST.get("Invoice_Client")
        invoice_order = request.POST.get("Invoice_Order")
        invoice_key = key_generator("Invoice")
        client = Client.objects.get(pk=invoice_client)
        print(invoice_client, invoice_order, client.Client_Name)
        context = {
            'invoice_client_id': client.Client_Id,
            'invoice_client_name': client.Client_Name,
            'invoice_order': invoice_order,
            'invoice_key': invoice_key,
            'form': form
        }
        return render(request, 'invoice/generate_invoice.html', context)


def add_new_client(request):
    if request.method == 'POST':
        form = New_Client_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client Added!')
            return HttpResponseRedirect(reverse('invoice'))

    form = New_Client_Form()
    context = {
        'form': form,
        'origin': 'Invoice'
    }
    return render(request, 'client/add_new_client.html', context)


def add_new_order(request):
    if request.method == "POST":
        form = New_Order_Form(request.POST)
        if form.is_valid():
            form.save()
            message.success(request, "Order Enlisted!")
            return HttpResponseRedirect(reverse('invoice'))

    form = New_Order_Form()
    context = {
        'form': form,
        'origin': 'Invoice'
    }
    return render(request, 'order/add_new_order.html', context)
