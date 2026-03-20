from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
from rest_framework.decorators import api_view,APIView,permission_classes,action
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import *
import razorpay
from django.conf import settings


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

    @action(detail=False, methods=['post'],url_path="add-item")
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
    

    @action(detail=False, methods=['get'],url_path="my-cart")
    def my_cart(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)
    

    @action(detail=False, methods=['post'],url_path="remove-item")
    def remove_item(self, request):
        product_id = request.data.get('product_id')

        cart = self.get_cart()

        try:
            item = CartItem.objects.get(cart=cart, product_id=product_id)
            item.delete()
            return Response({"message": "Item removed"})
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)
        


    @action(detail=False, methods=['post'],url_path='update-item')
    def update_item(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity'))

        cart = self.get_cart()

        try:
            item = CartItem.objects.get(cart=cart, product_id=product_id)
            item.quantity = quantity
            item.save()
            return Response({"message": "Item updated"})
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)
        

class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    # 🔒 Only logged-in user's addresses
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    # ✅ Auto assign user on create
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



@api_view(['POST'])
@permission_classes([IsAuthenticated])

def create_payment(request):
    try:
        amount = float(request.data.get('amount'))  # in INR

        # Convert to paise (Razorpay uses smallest currency unit)
        amount_paise = int(amount * 100)

        client = razorpay.Client(auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        ))

        payment_order = client.order.create({
            "amount": amount_paise,
            "currency": "INR",
            "payment_capture": 1
        })

        return Response({
            "message": "Payment order created",
            "order_id": payment_order['id'],
            "amount": payment_order['amount'],
            "currency": payment_order['currency']
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)
    


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # 🔒 Only user orders (admin sees all)
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    # ✅ Create Order from Cart
    @action(detail=False, methods=['post'],url_path="checkout")
    def checkout(self, request):

        user = request.user

        # Get user cart
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"error": "Cart is empty"}, status=400)

        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        total_amount = 0

        # Calculate total
        for item in cart_items:
            total_amount += item.product.price * item.quantity

        # Create Order
        order = Order.objects.create(
            user=user,
            total_amount=total_amount,
            status="PENDING",
            payment_id="PENDING",
            payment_type="COD"  # or Razorpay later
        )

        # Create Order Items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear cart
        cart_items.delete()

        serializer = self.get_serializer(order)
        return Response(serializer.data)