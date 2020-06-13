#source newenv/bin/activate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index(request, name="index"):
    if request.user.is_authenticated:
        return render(request, f"orders/{name}.html")
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
