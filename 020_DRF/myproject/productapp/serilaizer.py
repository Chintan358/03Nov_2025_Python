from rest_framework.serializers import *
from productapp.models import *

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'