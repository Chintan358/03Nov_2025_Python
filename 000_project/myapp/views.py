from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


def accounts(request):
    return render(request,"accounts.html")

def cart(request):
    return render(request,"cart.html")


def checkout(request):
    return render(request,"checkout.html")

def compare(request):
    return render(request,"compare.html")


def details(request):
    return render(request,"details.html")

def login_register(request):
    return render(request,"login-register.html")


def shop(request):
    return render(request,"shop.html")

def wishlist(request):
    return render(request,"wishlist.html")