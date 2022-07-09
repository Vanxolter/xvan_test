from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect, HttpResponse
import logging
from django.contrib.auth.models import User

from mainapp.forms import RegisterForm, Authorization, LinksForm
from mainapp.models import My_links

import string
import secrets

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
    if request.method == "POST":
        form = LinksForm(request.POST)
        if form.is_valid():
            logger.info(f"Пользователь {request.user} ввел ссылку {form.cleaned_data}")
            long_link: str = form.cleaned_data["long_link"]
            add_long_link = My_links.objects.create(author=request.user, long_link=long_link, short_link=None)
            cut_link1: list = long_link.split('//')  # Достаю "https:" из ссылки
            cut_link2: list = cut_link1[1].split('/')  # Достаю название сайта "www.youtube.com" из ссылки
            cropped_link: str = f"{cut_link1[0]}//{cut_link2[0]}/"  # Получаю рабочую домашнюю ссылку на сайт
            slug: str = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(6)) # Генерирую уникальный слаг
            short_link: str = f'{cropped_link}{slug}' # Моя короткая ссылка
            logger.info(f"Получаю короткую ссылку {short_link}")
            update = My_links.objects.filter(author=request.user, id=add_long_link.id).update(short_link=short_link) # Закидываю короткую ссылку в базу
            return render(request, "home.html", {"short_link": short_link, "form": form, "long_link": long_link})
    else:
        form = LinksForm()
        return render(request, 'home.html', {"form": form})


def my_links(request):
    return render(request, "links.html")