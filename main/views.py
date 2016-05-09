from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
import pytz

# Create your views here.

from forms import RegisterForm


def index(request):
    context = {"users": User.objects.all()}
    return render(request, 'index.html', context)


def register(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # print form

        print form.errors
        print form.is_valid();
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')

        else:
        	context = {}
        	context["form"] = form


    # if a GET (or any other method) we'll create a blank form
    else:
        context = {}
        form = RegisterForm()
        context["form"] = form
        context["timezones"] = pytz.all_timezones
        context["time_choices"] = ["test1", "test2"]

 
    return render(request, 'register.html', context)


def home(request):
	context = {}
	return render(request, 'home.html', context)

def settings(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SettingsForm(request.POST)
        # print form

        print form.errors
        print form.is_valid();
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')

        else:
            context = {}
            context["form"] = form


    # if a GET (or any other method) we'll create a blank form
    else:
        form = SettingsForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/home/")
        else:
            # Show an error page
            return HttpResponseRedirect("/account/invalid/")
    else:
        return render(request, 'login.html', {})


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/home/")