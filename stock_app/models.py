from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    user_group = models.ForeignKey(
        'UserGroup',
        on_delete=models.SET_NULL,
        null=True,
        related_name='apiusers'
    )

    def __str__(self):
        return self.email


class UserGroup(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name='Тип пользователя'
    )

    class Meta:
        verbose_name = 'Тип пользователя'
        verbose_name_plural = 'Типы пользователя'

    def __str__(self):
        return f'{self.pk}, {self.name}'


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
        return f'{self.pk}, {self.name}'

    def add_to_existing_product(self, product_in_store, quantity):
        new_quantity = quantity + product_in_store.quantity
        product_in_store.quantity = new_quantity
        product_in_store.save()

    def add_new_product(self, product, quantity):
        ProductInStore.objects.create(
            product=product,
            quantity=quantity,
            store=self
        )


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
        return f'{self.pk}, {self.name}'


class ProductInStore(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='products'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Кол-во на складе'
    )
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
        return f'{self.store.name}: ' \
               f'{self.product.name} - {str(self.quantity)} шт.'
