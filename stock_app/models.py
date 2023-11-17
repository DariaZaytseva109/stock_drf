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


class ProductInStore(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    store = models.ForeignKey(
        'Store',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )



