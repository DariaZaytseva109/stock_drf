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

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class ProductInStore(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,

    )
    quantity = models.PositiveIntegerField()
    store = models.ForeignKey(
        'Store',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )

    class Meta:
        verbose_name = 'Продукт на складе'
        verbose_name_plural = 'Продукты на складе'

    def __str__(self):
        return self.store.name + self.product.name + str(self.quantity)
