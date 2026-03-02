from django.urls import path
from empapp.views import *

urlpatterns = [
        path("all",EmpAPI.as_view()),
        path("all/<id>",EmpRetriveAPI.as_view())
]