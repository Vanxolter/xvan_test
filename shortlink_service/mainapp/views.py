from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect, HttpResponse
import logging
from django.contrib.auth.models import User

from mainapp.forms import RegisterForm, Authorization

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            logger.info(f"Пользователь {form.cleaned_data} зарегестрировался")
            user = User(
                username=form.cleaned_data["email"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password"])
            try:
                user.save()
                login(request, user)
                return redirect("main")
            except IntegrityError:
                return HttpResponse("Пользователь с такой почтой уже зарегистрирован")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def authorization(request):
    if "_signin" in request.POST:
        form = Authorization(request.POST)
        if form.is_valid():
            logger.info(f"Пользователь {form.cleaned_data} авторизировался")
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("main")
            else:
                return HttpResponse("Аккаунта не существует")
    elif "_reg" in request.POST:
        return redirect("/users/")
    else:
        form = Authorization()
        return render(request, "authorization.html", {"form": form})


def logout_view(request):
    logger.info(f"Пользователь {request.user} вышел из своего аккаунта")
    logout(request)
    return redirect("/")


def main(request):
    return render(request, "home.html")


def my_links(request):
    return render(request, "links.html")