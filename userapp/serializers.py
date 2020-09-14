from rest_framework import serializers
from rest_framework import exceptions
from userapp.models import Employee
from pro_drf03 import settings


class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    gender = serializers.IntegerField()
    pic = serializers.ImageField()