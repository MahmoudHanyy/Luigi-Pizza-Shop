#source newenv/bin/activate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request, name="index"):
    if request.user.is_authenticated:
        if name=='menu':
            pizzas = Pizza.objects.values()
            toppings = Topping.objects.values()
            subs = Sub.objects.values()
            pastas = Pasta.objects.values()
            salads = Salad.objects.values()
            dinnerplatters = DinnerPlatter.objects.values()
            context = {'salads': salads, 'dinnerplatters': dinnerplatters, 'pizzas':pizzas, 'pastas': pastas , 'subs':subs ,'toppings': toppings,'S_small': pizzas[0], 'S_Large': pizzas[1],'R_small': pizzas[2],'R_Large': pizzas[3]}
            return render(request, f"orders/{name}.html", context)
        else:
            return render(request, f"orders/{name}.html", context={})
    else:
        if name == 'register' :  return render(request, "orders/register.html")
        return render(request, "orders/login.html")

def login_view(request):
    password = request.POST['password']
    username = request.POST['username']

    user= authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html")

def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html")

    else:
         return HttpResponseRedirect(reverse("index"))

def cart(request):
    return HttpResponse('I am the cart')

def order(request):
    pizza = request.POST['pizza']
    topping1 = request.POST['topping1']
    topping2 = request.POST['topping2']
    topping3 = request.POST['topping3']
    subs = request.POST['subs']
    salad = request.POST['salads']
    pasta = request.POST['pastas']
    dinnerplatter= request.POST['dinnerplatter']

    pizza_quantity = request.POST["pizza-quantity"]
    salad_quantity = request.POST["salad-quantity"]
    pasta_quantity = request.POST["pasta-quantity"]
    dinnerplatter_quantity = request.POST["dinnerplatter-quantity"]

    return HttpResponse("Hello, Abdullah! "+pizza)
