from django.shortcuts import render
from .forms import New_Drawing_Form
from django.contrib import messages
from django.http import HttpResponseRedirect
from client.forms import New_Client_Form


def drawing(request):
    return render(request, 'drawing/drawing.html')


def add_new_drawing(request):
    if request.method == "POST":
        form = New_Drawing_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Drawing Enlisted!")
            return HttpResponseRedirect('/drawing')
        else:
            print(form.errors)

    form = New_Drawing_Form()
    context = {
        'form': form,
        'origin': 'drawing'
    }
    return render(request, 'drawing/add_new_drawing.html', context)


def add_new_client(request):
    if request.method == 'POST':
        form = New_Client_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client Added!')
            return HttpResponseRedirect('/design/add_new_drawing')

    form = New_Client_Form()
    context = {
        'form': form,
        'origin': 'Drawing'
    }
    return render(request, 'client/add_new_client.html', context)
