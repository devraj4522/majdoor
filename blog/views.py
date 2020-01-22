from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def services(request):
    return render(request, 'blog/services.html')

def contact(request):
    return render(request, 'blog/contact.html')

def login(request):
    return render(request, 'blog/login.html')

def register(request):
    return render(request, 'blog/register.html')

def menu(request):
    return render(request, 'blog/menu.html')