from rest_framework import serializers
from rest_framework import exceptions
from userapp.models import Employee
from pro_drf03 import settings


class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()
    gender = serializers.SerializerMethodField()
    pic = serializers.SerializerMethodField()

    def get_gender(self, obj):

        return obj.get_gender_display()

    def get_pic(self, obj):

        return f'{"http://127.0.0.1:8000"}{settings.MEDIA_URL}{obj.pic}'
