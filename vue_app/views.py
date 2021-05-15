from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from vue_app.models import Post  # , Login
from vue_app.forms import NewPost, NewUser


def feed(request):
    return render(request, 'vue_app/feed.html')

def login(request):
    return render(request, 'vue_app/login.html')

def new_user(request):

    context = {

    }

    return render(request, 'vue_app/new_user.html', context)

def new_user_FORM(request):
    # if this is a USER request we need to process the new user data
    if request.method == 'POST':
        # create a form instance and populate it with data from the data
        form = NewUser(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.create_user()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        else:
            return HttpResponseRedirect('/Error/')
    else:
        return HttpResponseRedirect('/Error/')
        # TODO Return Error View

def post(request, post_id):
    context = {
        'post': Post.objects.get(id=post_id)
    }
    if Post.objects.filter(id=post_id).exists()
        return render(request, 'vue_app/post/post_id',context )
    else:
        return HttpResponseRedirect('/Error')

def new_post(request):
    return render(request, 'vue_app/new_post.html')


def landing(request):
    return render(request, 'vue_app/landing.html')

def new_post_FORM(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewPost(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.create_post()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        else:
            return HttpResponseRedirect('/Error/')

    else:
        return HttpResponseRedirect('/Error/')
        # TODO Return Error View

