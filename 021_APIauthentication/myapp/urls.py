from django.urls import *
from myapp.views import *

urlpatterns = [
    path("create",create,name="create"),
    path("list",list,name="list"),
    path("retrive",retrive,name="retrive"),

    path("reg",reg,name="reg")
]