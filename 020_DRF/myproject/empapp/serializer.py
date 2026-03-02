from rest_framework.serializers import *
from empapp.models import *

class EmpSerializer(ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'
