from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("categories",CategoryViewSet)
router.register("products",ProductViewSet)
router.register("users",UserViewSet)
router.register("carts",CartViewSet)
router.register("address",AddressViewSet,basename="address"),
router.register('orders', OrderViewSet,basename="orders")
urlpatterns = [
      path('', include(router.urls)),
      path("payment",create_payment,name="payment")
]