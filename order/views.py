from django.shortcuts import render


def order(request):
	return render(request, 'order/order.html')


def add_new_order(request):
	return render(request, 'order/add_new_order.html')
