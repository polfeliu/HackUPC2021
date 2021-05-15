from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from vue_app.models import Post  # , Login
from vue_app.forms import NewPost


def feed(request):

    context = {
        'myvar': 'helooooo',
        'posts': Post.objects.all()
    }
    return render(request, 'vue_app/test.html', context)

def login(request):

    context = {

    }
    return render(request, 'vue_app/login.html', context)

def post(request, post_id):
    return HttpResponse(f"Hello, this is the {post_id}")

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

