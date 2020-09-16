from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, \
    DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView,\
    RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin,CreateModelMixin, UpdateModelMixin,DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from studentapp.models import Student
from userapp.models import Employee
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


class StudentGenericMixinView(ListAPIView,
                              RetrieveAPIView,
                              CreateAPIView,
                              DestroyAPIView,
                              UpdateAPIView,
                              ListCreateAPIView):
    queryset = Student.objects.filter(is_delete=False)
    serializer_class = StudentModelSerializer
    lookup_field = 'id'


class StudentModelViewSet(ModelViewSet):
    # queryset = Student.objects.filter(is_delete=False)
    # serializer_class = StudentModelSerializer
    # lookup_field = 'id'

    def user_login(self, request, *args, **kwargs):
        user_data = request.data
        print(user_data, type(user_data))
        user_obj = Employee.objects.filter(username=user_data.get('name'), password=user_data.get('pwd'))
        if user_obj:
            return APIResponse(data_message='登录成功')
        else:
            return APIResponse(data_status=400, data_message='登录失败')

    def user_register(self, request, *args, **kwargs):
        user_data = request.data
        try:
            user_obj = Employee.objects.create(username=user_data.get('name'), password=user_data.get('pwd'))
            return APIResponse(data_message='注册成功', results=user_obj)
        except:
            return APIResponse(data_status=400, data_message='注册失败')