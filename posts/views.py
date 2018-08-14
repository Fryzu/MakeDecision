from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .models import *

# Create your views here.

def main_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('METHOD POST - USER AUTHENTICATED')
        else:
            print('METHOD POST - USER NOT AUTHENTICATED')

    object_list = Post.objects.all()

    context = {
        "object_list": object_list,
    }

    return render(request, "main_view.html", context)

def post_details(request, requested_slug=None):
    instance = get_object_or_404(Post, slug=requested_slug)
    context = {
        "post": instance,
    }
    return render(request, "post_details.html", context)