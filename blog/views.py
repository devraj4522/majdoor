from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    parms = {'post': posts}

    return render(request, 'blog/index.html', parms)

def about(request):
    posts = Post.objects.all()
    parms = {'post': posts}
    return render(request, 'blog/about.html',parms)

def contact(request):
    return render(request, 'blog/contact.html')

def login(request):
    return render(request, 'blog/login.html')

def register(request):
    return render(request, 'blog/register.html')

def menu(request):
    return render(request, 'blog/menu.html')

def single(request):
    return render(request, 'blog/single.html')

def postView(request, name):
    post = Post.objects.filter(post_name = name)
    print(post)
    return render(request, "blog/post.html", {'post':post[0]})