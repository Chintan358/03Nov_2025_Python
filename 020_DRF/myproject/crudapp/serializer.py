from rest_framework.serializers import ModelSerializer
from crudapp.models import *

class StudentSerilaizer(ModelSerializer):
    class Meta :
        model = Student
        # fields = '__all__'
        # fields = ['id','name']
        exclude = ['name']