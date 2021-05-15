from django.shortcuts import render
from django.http import HttpResponse

from vue_app.models import Idea
#from vue_app.models import Login

def feed(request):

    context = {
        'myvar': 'helooooo',
        'posts': Idea.objects.all()
    }
    return render(request, 'vue_app/test.html', context)

def login(request):

    context = {

    }
    return render(request, 'vue_app/login.html', context)

def post(request, post_id):
    return HttpResponse(f"Hello, this is the {post_id}")