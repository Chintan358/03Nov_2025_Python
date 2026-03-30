from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def login(request):
    return render(request,"login.html")

def dologin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        try :
            st = student.objects.get(username=username,password=password)
            print(st)
            request.session['username']=st.username
            return redirect("home")
        except student.DoesNotExist:
             return render(request,"login.html",{"msg":"invalid credentials"})


def home(request):
    username = request.session.get("username")
    print(username)
    if username is None:
        return render(request,"login.html",{"msg":"Please login first"})
    return render(request,"home.html")

def logout(request):
    request.session.flush()
    return render(request,"login.html")