from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from productapp.serilaizer import *
from productapp.models import *
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer