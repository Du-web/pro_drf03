from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer

from studentapp.models import Student


class StudentListSerializer(serializers.ListSerializer):
    """
    群改序列化器
    """
    def update(self, instance, validated_data):
        for index, obj in enumerate(instance):
            self.child.update(obj, validated_data[index])
        return instance


class StudentModelSerializer(ModelSerializer):
    """
    序列化器整合
    """
    class Meta:
        list_serializer_class = StudentListSerializer
        model = Student
        fields = ('username', 'age', 'gender', 'phone', 'email', 'team_id')
        extra_kwargs = {
            'username': {
                'max_length': 6,
                'min_length': 2,
            },
            'team_id': {
                'write_only': True,
            }
        }

        def validate(self, attrs):
            name = attrs.get('username')
            book = Student.objects.filter(username=name)
            if len(book) > 0:
                raise exceptions.ValidationError('该学生已存在')
            return attrs