from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(request):
    if request.method=='POST':
        data = request.POST
        id = data['id']
        name = data['name']
        price = data['price']
        qty = data['qty'] 

        if id :
            pro = Product.objects.get(pk=id)
            pro.name = name
            pro.price = price
            pro.qty=qty
            pro.save()
            return render(request,"index.html",{"msg":"Product updated successfully !!!"})
        else:
            Product.objects.create(name=name,price=price,qty=qty)
            return render(request,"index.html",{"msg":"Product added successfully !!!"})
    

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})


def pro_delete(request):
    did = request.GET['did']
    pro = Product.objects.get(pk=did)
    pro.delete()
    return redirect("display")


def by_id(request):
    pid = request.GET['pid']
    pro = Product.objects.get(pk=pid)
   
    return render(request,"index.html",{"pro":pro})

