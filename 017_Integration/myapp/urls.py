from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("sendmail",sendmail,name="sendmail"),
    path("sendfile",sendfile,name="sendfile")
]