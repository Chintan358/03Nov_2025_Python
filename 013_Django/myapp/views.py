from django.shortcuts import render
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(request):
    if request.method=='POST':
        data = request.POST
        name = data['name']
        price = data['price']
        qty = data['qty']

            
        return render(request,"index.html",{"msg":"Product added successfully !!!"})