from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from empapp.models import *
from empapp.serializer import *

class EmpAPI(APIView):

    def get(self,request):
        emps = Emp.objects.all()
        ser = EmpSerializer(emps,many=True)
        return Response({"data":ser.data})
    
    def post(self,request):
        ser = EmpSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})


class EmpRetriveAPI(APIView):
    def get(self,request,id):
        emp = Emp.objects.get(id=id)
        ser = EmpSerializer(emp)
        return Response({"data":ser.data})

    def put(self,request,id):
        emp = Emp.objects.get(id=id)
        ser = EmpSerializer(emp,request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})

    def delete(self,request,id):
        emp = Emp.objects.get(id=id)
        emp.delete()
        return Response({"message":"emp deleted"})
