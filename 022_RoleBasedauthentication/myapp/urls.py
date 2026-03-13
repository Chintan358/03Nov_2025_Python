from django.urls import *
from myapp.views import *

urlpatterns = [
    path("student",get_student,name="student"),
    path("faculty",get_faculty,name="faculty"),
    path("reg",reg,name="reg")
]