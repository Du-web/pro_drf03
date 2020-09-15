from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from userapp.models import Book
from bookapp.serializers import BookModelSerializer, BookModelDeSerializer


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            # print(book_id)
            book_obj = Book.objects.get(pk=book_id)
            book_data = BookModelSerializer(book_obj).data
            # print(book_data)
            return Response({
                'status': 200,
                'message': '查询单个图书成功',
                'results': book_data
            })
        else:
            book_all = Book.objects.all()
            book_list = BookModelSerializer(book_all, many=True).data
            return Response({
                'status': 200,
                'message': '查询所有成功',
                'results': book_list
            })

    def post(self, request, *args, **kwargs):
        book_data = request.data
        if not isinstance(book_data, dict) or book_data == {}:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '请求的格式有误……'
            })
        book_ser = BookModelDeSerializer(data=book_data)
        book_ser.is_valid(raise_exception=True)
        book_obj = book_ser.save()
        return Response({
            'status': 200,
            'message': '创建图书成功',
            'results': BookModelSerializer(book_obj).data
        })