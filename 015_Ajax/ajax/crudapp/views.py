from django.shortcuts import render
from crudapp.models import *
from django.http import HttpResponse,JsonResponse
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