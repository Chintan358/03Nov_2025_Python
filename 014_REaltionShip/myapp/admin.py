from django.contrib import admin
from myapp.models import *
# Register your models here.

class CapitalModel(admin.ModelAdmin):
    list_display = ['name','country']

class ProductModel(admin.ModelAdmin):
    list_display = ['name','price','qty','category']

admin.site.register(Country)
admin.site.register(Capital,CapitalModel)

admin.site.register(Category)
admin.site.register(Product,ProductModel)

admin.site.register(Student)
admin.site.register(Subject)