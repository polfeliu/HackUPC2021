from django.shortcuts import render
from django.http import HttpResponse

def feed(request):
    return HttpResponse("Hello, this is the feed")

def post(request, post_id):
    return HttpResponse(f"Hello, this is the {post_id}")