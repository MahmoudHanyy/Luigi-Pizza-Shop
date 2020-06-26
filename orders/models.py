from django.db import models
from django.contrib.auth.models import User


SIZES = (
    ("S", "Small"),
    ("L", "Large")
)

STYLES = (
    ('R', 'Regular'),
    ('S', 'Sicilian')
)

# Create your models here.
class Topping(models.Model):
    """docstring for ."""
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Topping: {self.name}"


class Pasta(models.Model):
    """docstring for ."""
    name = models.CharField(max_length=32)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - $ {self.price}"

class Salad(models.Model):
    """docstring for ."""
    name = models.CharField(max_length=32)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - $ {self.price}"



class DinnerPlatter(models.Model):
    """docstring for ."""
    name = models.CharField(max_length=32)
    size = models.CharField(max_length=10, choices= SIZES)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.get_size_display()} - $ {self.price}"



class Pizza(models.Model):
    size = models.CharField(max_length=10, choices= SIZES)
    style = models.CharField(max_length=10, choices= STYLES)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2)
    toppings = models.ManyToManyField(Topping, blank=True)
    def __str__(self):
        #return f"{self.get_style_display()} - {self.get_size_display()} - {self.price} - Toppings: {self.toppings.in_bulk()}"
        return f"{self.size}"



class SubExtra(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - $ {self.price}"

class Sub(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices=SIZES)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2)
    extras = models.ManyToManyField(SubExtra, blank=True)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    sub = models.ManyToManyField(Sub, blank=True)
    pizza = models.ManyToManyField(Pizza, blank=True)
    pasta = models.ManyToManyField(Pasta, blank=True)
    salad = models.ManyToManyField(Salad, blank=True)
    dinnerplatter = models.ManyToManyField(DinnerPlatter, blank=True)

    def __str__(self):
            return f"{self.pizza.in_bulk()} - {self.pasta.in_bulk()} - {self.salad.in_bulk()}"
