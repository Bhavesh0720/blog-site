from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    con = {
        'form':form,
    }
    return render(request, 'register.html', con)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('home')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    con = {
        'form':form,
    }
    return render(request, 'login.html', con)


def logout(request):
    auth.logout(request)
    return redirect('login')
