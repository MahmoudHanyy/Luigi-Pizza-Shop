#source newenv/bin/activate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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
    cart = Cart.objects.filter(user=request.user, ordered=False).first()
    return HttpResponse(cart)

def order(request):
    products = ['Pizza', 'Pasta','Salad', 'Sub', 'Dinnerplatter']

    total = 0.0
    data = request.POST.copy()
    for product in products:

            if product == 'Pizza':
                try: pizza = Pizza.objects.get(id=int(data[product]))
                except: pizza = None
            if product == 'Pasta':
                try: pasta = Pasta.objects.get(id=int(data[product]))
                except: pasta= None
            if product == 'Salad':
                try: salad = Salad.objects.get(id=int(data[product]))
                except: salad= None
            if product == 'Sub':
                try: sub = Sub.objects.get(id=int(data[product]))
                except: sub= None
            if product == 'Dinnerplatter':
                try:   dinnerplatter = DinnerPlatter.objects.get(id=int(data[product]))

                except: dinnerplatter= None

    #create order object if not present
    order, created = Order.objects.get_or_create(
        pizza=pizza,
        pasta=pasta,
        salad=salad,
        dinnerplatter=dinnerplatter,
        sub=sub,
        pasta_quantity=data['pasta_quantity'],
        pizza_quantity=data['pizza_quantity'],
        salad_quantity=data['salad_quantity'],
        dinnerplatter_quantity=data['dinnerplatter_quantity'],
        user=request.user,
        ordered=False
    )

    if data['topping2'] != 'Select':
        topping = Topping.objects.get(id = int(data['topping2']))

        order.toppings.add(topping)
    if data['topping3'] != 'Select':
        topping = Topping.objects.get(id = int(data['topping3']))
        order.toppings.add(topping)

    if data['topping1'] != 'Select':
        topping = Topping.objects.get(id = int(data['topping1']))
        order.toppings.add(topping)

    else:
        topping = Topping.objects.get(name='Cheese')
        order.toppings.add(topping)
    #get cart of user
    try:
        cart = Cart.objects.filter(user=request.user, ordered=False).first()
        cart.order.add(order)

    #if cart_qs.exists():
    #    cart = cart_qs[0]

    except:
        cart = Cart.objects.create(user=request.user, ordered=False)
        cart.order.add(order)
        cart.save()
    #print(order)
    #print(cart)


    return redirect("cart/")
