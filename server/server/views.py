from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from account.models import UserInfo


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Signed in.")
        return redirect("/")
    else:
        messages.error(request, "Username or Password not correct.")
        return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")


def register_view(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        u = User.objects.create_user(username, email, password)
        i = UserInfo.objects.create(user=u)
        login(request, username=username, password=password)
        messages.success(request, "Welcome to Constant Time!")
        return redirect("/")
    except Exception as e:
        messages.error("An error occured when making the user:", str(e))
        return redirect("/")
