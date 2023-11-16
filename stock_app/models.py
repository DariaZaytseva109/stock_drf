from django.contrib.auth.models import AbstractUser

from django.db import models


class Store(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Наименование'
    )
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес'
    )


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование'
    )



