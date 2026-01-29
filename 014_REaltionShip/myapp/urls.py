from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("view",view_product,name="view")
]