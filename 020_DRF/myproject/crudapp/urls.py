from django.urls import path
from crudapp.views import *


urlpatterns = [
        path("list",list,name="list"),
        path("create",create,name="create"),
        path("retrive/<id>",retrive,name="retrive"),
        path("update/<id>",update,name="update"),
        path("delete/<id>",delete,name="delete")
]