from django.shortcuts import render
from product.models import Product
from design.models import Design
from producttype.models import ProductType
from .forms import New_Product_Form
from design.forms import New_Design_Form
from producttype.forms import New_ProductType_Form
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect


def product(request):
    product_data = Product.objects.filter().values(
        'Product_Id',
        'Product_Design__Design_Dimension',  # Only the pk (id) of the bug priority FK
        'Product_Price',
        'Product_Design__Design_Fpi',
        'Product_Type__Product_Type'
    )
    context = {
        'product_data': product_data
    }
    return render(request, "product/product.html", context)


def add_new_product(request):
    if request.method == "POST":
        form = New_Product_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Enlisted!")
            return HttpResponseRedirect('/product')
        else:
            print(form.errors)

    form = New_Product_Form()
    context = {
        'form': form,
        'origin': 'Product'
    }
    return render(request, 'product/add_new_product.html', context)


def add_new_design(request):
    if request.method == "POST":
        form = New_Design_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Design Enlisted!")
            return HttpResponseRedirect('/product')

    form = New_Design_Form()
    context = {
        'form': form,
        'origin': 'Product'
    }
    return render(request, 'design/add_new_design.html', context)


def add_new_producttype(request):
    if request.method == "POST":
        form = New_ProductType_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Type Enlisted!")
            return HttpResponseRedirect('/product/add_new_product')

    form = New_ProductType_Form
    context = {
        'form': form,
        'origin': 'Product'
    }
    return render(request, 'producttype/add_new_producttype.html', context)
