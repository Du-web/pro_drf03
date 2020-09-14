from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from userapp.models import Employee
from userapp.serializers import EmployeeSerializer,EmployeeDeSerializer


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

    def post(self, request, *args, **kwargs):
        """
        接收数据并保存在数据库
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        emp_data = request.data
        if not isinstance(emp_data, dict) or emp_data == {}:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '请求数据格式有误'
            })
        ser = EmployeeDeSerializer(data=emp_data)
        if ser.is_valid():
            emp = ser.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': '用户保存成功',
                'results': EmployeeSerializer(emp).data
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': ser.errors
        })
