from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
from rest_framework.decorators import api_view,APIView,permission_classes,action
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import *


class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def get_permissions(self):
       
        if self.action in ['list']:
            permission_classes=[IsAdminUser]
        elif self.action in ['create']:
            permission_classes=[AllowAny]
        elif self.action in ['update','destroy','retrieve']:
            permission_classes=[IsAuthenticated]
        else:
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]
   
class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    def get_permissions(self):
       
        if self.action in ['list','retrieve']:
            permission_classes=[AllowAny]
        elif self.action in ['create','update','destroy']:
            permission_classes=[IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    @action(detail=False, methods=['get'], url_path='by-category/(?P<category_id>[^/.]+)')
    def by_category(self, request, category_id=None):
        products = Product.objects.filter(category_id=category_id)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    def get_permissions(self):
       
        print(self.action)
        if self.action in ['list','retrieve','by_category']:
            permission_classes=[AllowAny]
        elif self.action in ['create','update','destroy']:
            permission_classes=[IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_cart(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

    @action(detail=False, methods=['post'])
    def add_item(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        
        cart = self.get_cart()

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

        return Response({"message": "Item added to cart"})