from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from userapp.models import Employee
from userapp.serializers import EmployeeSerializer


class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        if user_id:
            emp = Employee.objects.get(pk=user_id)
            emp_ser = EmployeeSerializer(emp).data

            return Response({
                'status': 200,
                'message': '查询单个成功',
                'results': emp_ser
            })
        else:
            emps = Employee.objects.all()
            emps_ser = EmployeeSerializer(emps, many=True).data
            return Response({
                'status': 200,
                'message': '查询所有成功',
                'results': emps_ser
            })
