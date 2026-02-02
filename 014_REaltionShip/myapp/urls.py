from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("view",view_product,name="view"),
    path('delete',delete_product,name="delete"),
    path('edit',edit_product,name="edit")
]