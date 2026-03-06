from django.urls import path
from relationapp.views import *


urlpatterns = [
    path("create",create_product,name="create"),
    path("list",list_product,name="list")
]