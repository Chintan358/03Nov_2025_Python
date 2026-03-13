from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from myapp.permission import *
from myapp.serializer import *
# Create your views here.

@api_view(['GET'])
@permission_classes([IsStudent])
def get_student(request):
    return Response({"message":"student api calling"})


@api_view(['GET'])
@permission_classes([IsFaculty])
def get_faculty(request):
    return Response({"message":"faculty api calling"})



@api_view(['POST'])
def reg(request):
    print(request.data)
    ser= UserSerializer(data=request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})