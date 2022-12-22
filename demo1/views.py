from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from demo1.forms import NEWUSER
from demo1.forms import registerform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def userview(request):
    form = NEWUSER()
    if request.method == 'POST':
        form = NEWUSER(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/')
    return render(request, 'register.html', {'form': form})


def registeruserview(request):
    form = registerform()
    if request.method == 'POST':
        form = registerform(request.POST)
        if request.POST['password'] == request.POST['password2']:
            if form.is_valid():
                form.save()
                print("haii")
                return redirect('/login/')
    return render(request, 'register.html', {'form': form})


def loginview(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            pass1 = form.cleaned_data['password']
            us = authenticate(username=user, password=pass1)
            if us is not None:
                login(request, us)
                print(us)
                return redirect('/home/')
    return render(request, 'login1.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('/home/')


def welcome(request):
    return render(request, 'welcome.html')
