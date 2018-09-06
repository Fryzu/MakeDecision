from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm

# Create your views here.

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("main_view"))

def signup_view(request):
    # TODO: User form input corectness
    #if request.method == "POST":
    #    username = request.POST['username']
    #    password = request.POST['password']
    #    first_name = request.POST['first_name']
    #    last_name = request.POST['last_name']
    #    email = request.POST['email']
    #    checkbox = request.POST['checkbox']
    #    if checkbox == "on":
    #        User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("main_view"))
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'signup_view.html', context)