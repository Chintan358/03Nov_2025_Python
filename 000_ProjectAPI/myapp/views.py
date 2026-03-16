from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.viewsets import ModelViewSet



class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

