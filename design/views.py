from django.shortcuts import render
from .forms import New_Design_Form
from drawing.forms import New_Drawing_Form
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect


def design(request):
    return render(request, 'design/design.html')


def add_new_design(request):
    if request.method == "POST":
        form = New_Design_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Design Enlisted!")
            return HttpResponseRedirect('/design')
        else:
            print(form.errors)

    form = New_Design_Form()
    context = {
        'form': form,
        'origin': 'Design'
    }
    return render(request, 'design/add_new_design.html', context)


def add_new_drawing(request):
    if request.method == "POST":
        form = New_Drawing_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Drawing Enlisted!")
            return HttpResponseRedirect('/product/add_new_design')
        else:
            print(form.errors)

    form = New_Drawing_Form()
    context = {
        'form': form,
        'origin': 'design'
    }
    return render(request, 'drawing/add_new_drawing.html', context)

