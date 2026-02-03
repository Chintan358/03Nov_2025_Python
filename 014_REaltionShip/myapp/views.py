from django.shortcuts import render,redirect
from myapp.models import *
import os
# Create your views here.
def index(request):
   
    if request.method=='POST':
        
        data = request.POST
        category = Category.objects.get(pk=data['category'])
        name = data['name']
        price = data['price']
        qty = data['qty']
        file = None
        if request.FILES :
            file = request.FILES['file']


        Product.objects.create(category=category,name=name,price=price,qty=qty,image=file)

    categories = Category.objects.all()
    return render(request,"index.html",{"categories":categories})


def view_product(request):
    products = Product.objects.all()
    return render(request,"view.html",{"products":products})

def delete_product(request):
    did= request.GET['did']
    product = Product.objects.get(pk=did)
    product.delete()
    if product.image:
        os.remove(product.image.path)
    return redirect("view")

def edit_product(request):
    eid = request.GET['eid']
    product = Product.objects.get(pk=eid)
    categories = Category.objects.all()
    if request.method=='POST':       
        data = request.POST
        category = Category.objects.get(pk=data['category'])
        name = data['name']
        price = data['price']
        qty = data['qty']
        file = None
        if request.FILES :
            if product.image:
                os.remove(product.image.path)
            file = request.FILES['file']
            product.image = file

        product.category = category
        product.name = name
        product.price = price
        product.qty = qty
        
        product.save()

        return render(request,"index.html",{"categories":categories})
  
    
    return render(request,"index.html",{"product":product,"categories":categories})