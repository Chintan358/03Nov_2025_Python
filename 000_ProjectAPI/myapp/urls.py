from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("categories",CategoryViewSet)
router.register("products",ProductViewSet)
router.register("users",UserViewSet)
router.register("carts",CartViewSet)
urlpatterns = [
      path('', include(router.urls)),
]