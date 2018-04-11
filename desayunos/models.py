from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Bar(models.Model):
    name = models.CharField(max_length=70)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Group(models.Model):
    code = models.CharField(max_length=5, blank=True)
    name = models.CharField(max_length=70)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class ProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=50)
    basePrice = models.FloatField()
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Menu(models.Model):
    name = models.CharField(max_length=50)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    product = JSONField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Modifier(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='PivotModifierProduct')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class PivotModifierProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    modifier = models.ForeignKey(Modifier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.price

    class Meta:
        ordering = ['price']


class Order(models.Model):
    OrderStateChoice = (
        ('Checked', 'Checked'),
        ('NotChecked', 'NotChecked'),
    )

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    state = models.CharField(max_length=30, choices=OrderStateChoice)

    def __str__(self):
        return self.state
