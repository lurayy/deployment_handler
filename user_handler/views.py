from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, LoginForm

def user_login(request):
    if request.user.is_authenticated:
        return True
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponse("Username or password doesn't match")
        return HttpResponse("Invalid Form.")

def user_register(request):
    if request.user.is_authenticated:
        return True
    if request.method == "GET":
        form = UserCreationForm()
        return render (request, 'register.html',{'form':form})
    else:
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
