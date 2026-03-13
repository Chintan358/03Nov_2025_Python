from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from myapp.serializer import *
from myapp.permissions import IsStaffUser


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create(request):
    return Response("Create api calling")


@api_view(['GET'])
@permission_classes([IsStaffUser])
def list(request):
    return Response("list api calling")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrive(request):
    return Response("Retrive api calling")

@api_view(['POST'])
def reg(request):
    ser= UserSerializer(data=request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})