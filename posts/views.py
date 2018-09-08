from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import datetime

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
    instance_answers = Answer.objects.all().filter(post=instance)

    #checking in cookies if voted in this post
    cookie_string = 'voted:%s' %(instance._id)
    voted = cookie_string in request.COOKIES

    context = {
        "post": instance,
        "answers": instance_answers,
        "voted": voted,
    }      

    return render(request, "post_details.html", context)

def increment_answer_count(request, requested_answer_id):
    instance = get_object_or_404(Answer, id=requested_answer_id)
    response =  HttpResponseRedirect(instance.post.get_absolute_url())

    #checking in cookies if voted in this post
    cookie_string = 'voted:%s' %(instance.post._id)
    voted = cookie_string in request.COOKIES
    
    if not voted:
        instance.count += 1
        instance.save()
        response.set_cookie(cookie_string, datetime.datetime.now())

    return response