from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Capital(models.Model):
    country = models.OneToOneField(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)

    
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="images",null=True)


class Student(models.Model):
    name = models.CharField(max_length=20)

class Subject(models.Model):
    student = models.ManyToManyField(Student)
    name = models.CharField(max_length=20)