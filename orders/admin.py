from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Topping)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Pizza)
admin.site.register(SubExtra)
admin.site.register(Sub)
admin.site.register(Order)
admin.site.register(Cart)
