from django.urls import path,include
from myapp.views import *

urlpatterns = [
        path("list/",get_data,name="list"),
        path("create/",add_data,name="create"),
        path("update/",update_data,name="update"),
        path("delete/",delete_data,name="delete")

]