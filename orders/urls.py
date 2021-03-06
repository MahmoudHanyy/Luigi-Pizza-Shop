from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("<name>", views.index, name="index"),
    path("order/", views.order, name="order"),
    path("order/cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),

]
