from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("login",login_page,name="login"),
    path("home",home, name="home"),
    path("logout",logout_page,name="logout")
]