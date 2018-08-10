from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

# Create your views here.

def main_view(request):
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