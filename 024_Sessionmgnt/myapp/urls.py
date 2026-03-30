from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",login,name="login"),
    path("home",home,name="home"),
    path("logout",logout,name="logout"),
    path("dologin",dologin,name="dologin")
]