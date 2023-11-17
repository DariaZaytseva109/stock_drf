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

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование'
    )

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.store.name + self.product.name + str(self.quantity)



