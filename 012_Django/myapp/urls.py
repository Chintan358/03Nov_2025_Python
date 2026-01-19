from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("contact",contact,name="contact")
]