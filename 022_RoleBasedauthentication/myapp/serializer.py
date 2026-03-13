from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from myapp.models import *


class RoleSerilizer(ModelSerializer):
    class Meta:
        model = Role
        fields='__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = '__all__'

    def create(self, validated_data):
        
        u = CustomeUser.objects.create_user(phone=validated_data['phone'],password=validated_data['password'])
        return u