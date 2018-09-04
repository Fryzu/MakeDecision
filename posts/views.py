from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .models import *

# Create your views here.

def main_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.add_message(request, messages.ERROR, 'Incorrect username or password.')

    object_list = Post.objects.all()[:3]

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