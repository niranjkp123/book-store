from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=222)
    author = models.CharField(max_length=222)
    description = models.CharField(max_length=555)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2222, blank=True)
    follow_author = models.CharField(max_length=2222, blank=True)
    book_available = models.BooleanField()
    star = models.FloatField()

class Register(models.Model):
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)

class Login(models.Model):
    username = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)

class Order(models.Model):
    product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title  # Updated to access the product's title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2222, blank=True) # ImageField for cart image
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
