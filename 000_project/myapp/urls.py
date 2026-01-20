from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("accounts",accounts,name="accounts"),
    path("cart",cart,name="cart"),
     path("checkout",checkout,name="checkout"),
    path("compare",compare,name="compare"),
      path("details",details,name="details"),
    path("login-register",login_register,name="login-register"),
     path("shop",shop,name="shop"),
    path("wishlist",wishlist,name="wishlist"),
]