from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


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
        return f"{self.name}"


class Pasta(models.Model):
    """docstring for ."""
    name = models.CharField(max_length=32)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class Salad(models.Model):
    """docstring for ."""
    name = models.CharField(max_length=32)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}"



class DinnerPlatter(models.Model):
    """docstring for ."""
    name = models.CharField(max_length=32)
    size = models.CharField(max_length=10, choices= SIZES)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name},{self.get_size_display()}"



class Pizza(models.Model):
    size = models.CharField(max_length=10, choices= SIZES)
    style = models.CharField(max_length=10, choices= STYLES)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.get_style_display()},{self.get_size_display()}"




class SubExtra(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class Sub(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices=SIZES)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2)
    extras = models.ManyToManyField(SubExtra, blank=True)

    def get_total(self):
        total = self.price
        try:
            for extra in self.extras.all():
                total += extras.price
        except: pass


    def __str__(self):
        return f"{self.name}-{self.size}-Extras: {self.extras.in_bulk()}"



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    sub = models.ForeignKey(Sub, on_delete=models.CASCADE, blank=True, null=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, null=True)
    toppings = models.ManyToManyField(Topping, blank=True, related_name='toppings')
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE, blank=True, null=True)
    salad = models.ForeignKey(Salad, on_delete=models.CASCADE, blank=True, null=True)
    dinnerplatter = models.ForeignKey(DinnerPlatter, on_delete=models.CASCADE, blank=True, null=True)

    pizza_quantity = models.IntegerField(default = 0)
    salad_quantity = models.IntegerField(default = 0)
    pasta_quantity = models.IntegerField(default = 0)
    dinnerplatter_quantity = models.IntegerField(default = 0)

    def __str__(self):
        order_string = f"order: "
        if self.pizza: order_string+= 'Pizza: '+self.pizza.__str__()+','
        if self.toppings: order_string+= 'Topping: '+','.join([str(top) for top in self.toppings.all()])
        if self.pasta: order_string+= 'Pasta: '+self.pasta.__str__()+','
        if self.salad: order_string+= 'Salad: '+self.salad.__str__()+','
        if self.sub: order_string+= 'Sub: '+self.sub.__str__()+','
        if self.dinnerplatter: order_string+= 'DinnerPlatter: '+self.dinnerplatter.__str__()+','

        return f"Total of:  {self.get_total_price()} for {order_string}"

    def get_total_price(self):
        total = 0
        if self.pizza: total += self.get_pizza_price()
        if self.pasta: total+= float(self.pasta.price) * float(self.pasta_quantity)
        if self.salad: total+= float(self.salad.price) * float(self.salad_quantity)
        if self.sub: total+= float(self.sub.price)
        if self.dinnerplatter: total+= float(self.dinnerplatter.price) * float(self.dinnerplatter_quantity)
        return total

    def get_pizza_price(self):
        pizza_total = 0.0
        toppings_choices = {'Sicilian_Small': {'1': 26.45, '2':28.45, '3': 29.45}, 'Sicilian_Large': {'1': 40.70, '2': 42.70, '3': 44.70}, 'Regular_Small': {'1':13.70, '2': 15.20, '3': 16.20}, 'Regular_Large': {'1': 19.95, '2': 21.95, '3': 23.95}}
        if len(self.toppings.all()) == 1:
            if self.toppings.all().first().name == 'Cheese':
                return float(self.pizza.price) * int(self.pizza_quantity)
        else:
            return toppings_choices[f"{self.pizza.get_style_display()}_{self.pizza.get_size_display()}"][str(len(self.toppings.all())-1)] * float(self.pizza_quantity)



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    order = models.ManyToManyField(Order, related_name='orders')
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} Charge is -{self.get_total()}- {self.order.in_bulk()}"

    def get_total(self):
        total = 0
        for order in self.order.all():
            total += order.get_total_price()
        return round(total)
