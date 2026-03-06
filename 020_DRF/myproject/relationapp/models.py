from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=20)

class Address(models.Model):
    adr = models.CharField(max_length=50)

class Company(models.Model):
    adr = models.ForeignKey(Address,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
