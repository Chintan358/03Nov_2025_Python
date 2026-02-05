from django.urls import path
from crudapp.views import *

urlpatterns = [
    path("",index,name="index1"),
    path("reg",reg,name="reg"),
    path("display",display,name="display"),
    path("delete",delete_student,name="delete"),
    path("stbyid",stbyid,name="stbyid")
]