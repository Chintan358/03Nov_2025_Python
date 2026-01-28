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

        Product.objects.create(category=category,name=name,price=price,qty=qty)

    categories = Category.objects.all()
    return render(request,"index.html",{"categories":categories})