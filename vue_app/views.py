from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login as user_login
from django.contrib import messages

from vue_app.models import Post
from vue_app.forms import NewPost, NewUserForm

# TODO Protect view from unauthenticated users

def feed(request):
    return render(request, 'app/feed.html')

def login(request):
    return render(request, 'app/login.html')

def new_user(request):

    context = {

    }

    return render(request, 'app/new_user.html', context)

def register_FORM(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            messages.success(request, "Registration successful.") # TODO Display to front end
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def post(request, post_id):

    if Post.objects.filter(id=post_id).exists():
        context = {
            'post': Post.objects.get(id=post_id)
        }
        return render(request, 'app/post.html', context)
    else:
        return HttpResponseRedirect('/Error')

def new_post(request):
    return render(request, 'app/new_post.html')


def landing(request):
    return render(request, 'landing.html')

def new_post_FORM(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewPost(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post_id = form.create_post()
            # redirect to a new URL:
            return HttpResponseRedirect(f'/post/{post_id}')

        else:
            return HttpResponseRedirect('/Error/')

    else:
        return HttpResponseRedirect('/Error/')
        # TODO Return Error View

