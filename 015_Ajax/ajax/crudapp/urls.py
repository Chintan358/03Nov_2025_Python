from django.urls import path
from crudapp.views import *

urlpatterns = [
    path("",index,name="index1")
]