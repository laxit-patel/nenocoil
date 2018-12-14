from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from login.models import User


# disabling csrf (cross site request forgery)
@csrf_exempt
def login(request):
    return render(request, 'login/login.html')


def dashboard(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        user_email = request.POST.get('user_email')
        password = request.POST.get('user_password')

        user_name = User.objects.all().values('User_Name')

        # adding the values in a context variable
        context = {
            'user_name': user_name,
            'user_email': user_email,
            'password': password,

        }

        # getting our showdata template
        template = loader.get_template('dashboard/dashboard.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        # if post request is not true
        # returning the form template
        template = loader.get_template('login/login.html')
        return HttpResponse(template.render())


