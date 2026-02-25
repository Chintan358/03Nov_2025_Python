from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_data(request):
    return Response({'message': 'Hello from DRF!'})

@api_view(['POST'])
def add_data(request):
    return Response({"message":"Post api calling"})


@api_view(['PUT'])
def update_data(request):
    return Response({'message': 'PUt calling'})

@api_view(['DELETE'])
def delete_data(request):
    return Response({"message":"delete api calling"})