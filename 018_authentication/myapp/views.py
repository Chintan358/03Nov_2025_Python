from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get("fname")
        lname = data.get("lname")
        uname = data.get("uname")
        password = data.get("pass")

        if User.objects.filter(username = uname).exists():
             return render(request,"index.html",{"err":"Username already exist"})

        user = User(first_name = fname,last_name=lname,username=uname)
        user.set_password(password)
        user.save()

        return render(request,"index.html",{"msg":"Registration successfully"})

    print("hello")
    return render(request,"index.html")

def login_page(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get("uname")
        password = data.get("pass")

       


        user = authenticate(username=uname,password=password)
        if user is None:
            return render(request,"login.html",{"err":"Invalid credentials"})
        else:
            login(request,user)
            return redirect("home")

    if request.user.is_authenticated:
        return redirect("home")
    return render(request,"login.html")


@login_required(login_url="login")
def home(request):
    return render(request,"home.html")


def logout_page(request):
    logout(request)
    return render(request,"login.html")