from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class My_links(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="routs")
    long_link: str = models.URLField(verbose_name="Длинная ссылка", null=True, blank=True)
    short_link: str = models.URLField(verbose_name="Короткая ссылка", null=True, blank=True)


