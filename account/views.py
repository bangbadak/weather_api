from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import UserForm


def register(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('show_info')
    else:
        form = UserForm()
    return render(request, 'account/register.html', {'form': form})

def Login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username, password)
            login(request, user)
            return redirect('show_info')
    else:
        form = UserForm()
    return render(request, 'account/Login.html', {'form': form})

def find_password(request):
    return render(request, 'show_info/index.html')
