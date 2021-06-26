from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from show_info.views import index
from django.contrib import auth

def register(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
            user.save()
            login(request, user)
            return render(request, 'account/signin.html')
        return render(request, 'account/register.html')
    return render(request, 'account/register.html')
  
def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('show_info')
        else:
            return render(request, 'account/signin.html', {'error': 'email or password is incorrect'})
    else:
        return render(request, 'account/signin.html')

def find_password(request):
    return render(request, 'show_info/index.html')
