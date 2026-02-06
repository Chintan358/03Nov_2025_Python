from django.shortcuts import render
from crudapp.models import *
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"home.html")

def reg(request):
    if request.method=="POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")

        Student.objects.create(name=name,email=email,phone= phone)

        return HttpResponse("Registration successfully !!!")
    
def display(request):
    students = Student.objects.all()
    return JsonResponse({"students":list(students.values())})

def delete_student(request):
    sid = request.GET['sid']
    student = Student.objects.get(pk=sid)
    student.delete()
    return HttpResponse("Student deleted !!!")

def stbyid(request):
    sid = request.GET['sid']
    student = Student.objects.filter(id=sid)
    return JsonResponse({"student":list(student.values())})

def update_student(request):
     if request.method=="POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")

        std = Student.objects.get(pk=id)
        std.name = name
        std.email = email
        std.phone  =phone
        std.save()

        return HttpResponse("Student updated !!!")
     

def search(request):
    q = request.GET['q']
    # students = Student.objects.filter(name__startswith=q) or  Student.objects.filter(email__startswith=q) or  Student.objects.filter(phone__startswith=q)


    students = Student.objects.filter(Q(name__startswith=q) | Q(email__startswith=q) | Q(phone__startswith=q)) 

    return JsonResponse({"students":list(students.values())})


def checkemail(request):
    email = request.GET['email']
    result =  Student.objects.filter(email=email).exists()
    return HttpResponse(result)