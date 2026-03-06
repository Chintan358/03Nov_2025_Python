from rest_framework.serializers import ModelSerializer
from relationapp.models import *
class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'


    def to_representation(self, instance):
        response =  super().to_representation(instance)
        response['adr'] = AddressSerializer(instance.adr).data
        return response

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
    def to_representation(self, instance):
        response =  super().to_representation(instance)
        response['category']=CategorySerializer(instance.category).data
        response['company']=CompanySerializer(instance.company).data
        return response