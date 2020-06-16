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
            print(pizzas[1]['id'])
            context = {'S_small': pizzas[0], 'S_Large': pizzas[1],'R_small': pizzas[2],'R_Large': pizzas[3]}
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



def order(request, id):
    pizza= Pizza.objects.get(pk=id)
    print(pizza)
    return HttpResponse("Hello, Abdullah!")
