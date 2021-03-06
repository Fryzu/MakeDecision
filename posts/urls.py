"""bsa_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', main_view, name="main_view"),
    re_path(r'^questions/(?P<requested_slug>[a-z0-9-]+)$', post_details, name='post_details'),
    re_path(r'^questions/increment_answer_count/(?P<requested_answer_id>[0-9]+)$', increment_answer_count, name='increment_answer_count')
]