from django.urls import path
from myapp.views import *

urlpatterns = [
      path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("display",display,name="display"),
    path("delete",pro_delete,name="delete"),
    path("byid",by_id,name="byid")
]