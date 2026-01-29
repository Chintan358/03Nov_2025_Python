from django.shortcuts import render
from myapp.models import *
# Create your views here.
def index(request):
   
    if request.method=='POST':
        
        data = request.POST
        category = Category.objects.get(pk=data['category'])
        name = data['name']
        price = data['price']
        qty = data['qty']
        file = request.FILES['file']


        Product.objects.create(category=category,name=name,price=price,qty=qty,image=file)

    categories = Category.objects.all()
    return render(request,"index.html",{"categories":categories})


def view_product(request):
    products = Product.objects.all()
    return render(request,"view.html",{"products":products})