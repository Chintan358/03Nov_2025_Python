from django.contrib import admin
from myapp.models import *
# Register your models here.

class StudentData(admin.ModelAdmin):
    list_display=["id","name","email","phone","age","fees","dob","info","gender"]
