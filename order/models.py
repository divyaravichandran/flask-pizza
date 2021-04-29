from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Regular_Pizza(models.Model):
    name = models.CharField(max_length=32)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"

class Sicilian_Pizza(models.Model):
    name = models.CharField(max_length=32)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"

class Toppings(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"

class Subs(models.Model):
    name = models.CharField(max_length=32)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"


class Pasta(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Dinner_Platter(models.Model):
    name = models.CharField(max_length=32)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"

class Shopping_Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shopping")
    item = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=32)
    status = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} - {self.item} - {self.category} - {self.price} - {self.status}"

class Order(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    order_details = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"
