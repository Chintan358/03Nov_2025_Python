from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("search",search, name="search"),
    path("countries",countries,name="countries"),
    path("states",states,name="states")
]