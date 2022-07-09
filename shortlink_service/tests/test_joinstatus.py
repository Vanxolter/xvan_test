from django.test import Client
import pytest
from django.contrib.auth.models import User

from mainapp.models import My_links


@pytest.mark.django_db
class TestCreateUser:
    def test_createuser(self):
        client = Client()

        # Тест Тест на статус страницы регистрации
        response = client.get("/register/")
        assert response.status_code == 200

        # Тест по созданию юзера
        user = User.objects.create(first_name="test", last_name="test2", email="test@test.com", password="test")
        client.force_login(user)

        # Тест на добавление ссылки в базу
        link = My_links.objects.create(author=user, long_link=None, short_link=None)
        assert response.status_code == 200

        # Тест на добавление ссылки в базу
        link = My_links.objects.create(author=user, long_link="fdsfds", short_link="fdsfds")
        assert response.status_code == 200

        # Тест на статус авторизации
        response = client.get("")
        assert response.status_code == 200

        # Тест на статус страниццы ссылок
        response = client.get("/links/")
        assert response.status_code == 200

        # Тест на статус главной
        response = client.get("/main/")
        assert response.status_code == 200

