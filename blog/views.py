from django.shortcuts import render
from invoice.models import

def blog(request):
    return render(request, 'blog/blog.html')
