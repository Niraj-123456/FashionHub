from django.db import models
from django import forms
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    img_path = models.FilePathField(path='./static/img/')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    img_path = models.FilePathField(path='./static/img/products/')
    description = models.CharField(max_length=500, default="No description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    completed = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200)
    OPTIONS = (
        ('pending', 'pending'),
        ('delivered', 'delivered')
    )
    delivered = models.CharField(max_length=10, choices=OPTIONS)

class OrderItem(models.Model):
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)




