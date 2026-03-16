from django.urls import *
from productapp.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('all', ProductViewSet)


urlpatterns = router.urls