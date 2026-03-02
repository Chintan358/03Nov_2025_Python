from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from crudapp.models import *
from crudapp.serializer import StudentSerilaizer
from rest_framework import status
#list : view all data

@api_view(['GET'])
def list(request):
    all = Student.objects.all()
    ser = StudentSerilaizer(all,many=True)
    return Response({"data":ser.data})

#create : create or add data
@api_view(['POST'])
def create(request):
    data = request.data
    ser = StudentSerilaizer(data = data)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
    else :
        ser.save()
        return Response({"data":ser.data,"message":"Success"})


#retrive :view data by id
@api_view(['GET'])
def retrive(request,id):
    try : 
        student = Student.objects.get(pk=id)
        ser = StudentSerilaizer(student)
        return Response({"data":ser.data})
    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_404_NOT_FOUND)
    
#update  :update data
@api_view(['PUT'])
def update(request,id):
    try : 
        student = Student.objects.get(pk=id)
        ser = StudentSerilaizer(student,request.data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"Something went wrong"})
        else :
            ser.save()
            return Response({"data":ser.data,"message":"Success"})

    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_404_NOT_FOUND)
#delete : delete data
@api_view(['DELETE'])
def delete(request,id):
    try : 
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"message":"Data deleted"})
    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_404_NOT_FOUND)
