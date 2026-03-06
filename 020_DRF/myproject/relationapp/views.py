from django.shortcuts import render
from rest_framework.response import Response
from relationapp.models import *
from relationapp.serializer import *
from rest_framework.decorators import api_view,APIView

@api_view(['POST'])
def create_product(request):
    ser = ProductSerializer(data=request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})

@api_view(['GET'])
def list_product(request):
    all = Product.objects.all()
    ser = ProductSerializer(all,many=True)
    return Response({"data":ser.data})