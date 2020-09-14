from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView


class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):

        return Response({
            'status': 200,
            'message': '查询成功'
        })