from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, \
    DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView,\
    RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin,CreateModelMixin, UpdateModelMixin,DestroyModelMixin
from rest_framework.response import Response

from studentapp.models import Student
from studentapp.serializers import StudentModelSerializer
from utils.response import APIResponse


class StudentGenericAPIView(GenericAPIView,
                            ListModelMixin,
                            RetrieveModelMixin,
                            CreateModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin):

    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentModelSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        # stu_id = kwargs.get('id')
        # if stu_id:
        #     stu_obj = self.get_object()
        #     many = False
        # else:
        #     stu_obj = self.get_queryset()
        #     many = True
        # stu_ser = self.get_serializer(stu_obj, many=many).data
        # return APIResponse(results=stu_ser)
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        create = self.create(request, *args, **kwargs)
        return APIResponse(results=create.data, data_message='添加成功')

    def put(self, request, *args, **kwargs):
        res = self.update(request, *args, **kwargs)
        return APIResponse(results=res.data)

    def patch(self, request, *args, **kwargs):
        res = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=res.data)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(data_message='删除成功')



