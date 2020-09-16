from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from userapp.models import Book
from bookapp.serializers import BookModelSerializer, BookModelDeSerializer, BookModelSerializerV2


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


class BookAPIViewV2(APIView):

    def get(self, request, *args, **kwargs):

        book_id = kwargs.get('id')
        if book_id:
            book_obj = Book.objects.get(pk=book_id, is_delete=False)
            book_data = BookModelSerializer(book_obj).data
            return Response({
                'status': 200,
                'message': '查询单个图书成功',
                'results': book_data
            })
        else:
            book_all = Book.objects.filter(is_delete=False)
            book_list = BookModelSerializer(book_all, many=True).data
            return Response({
                'status': 200,
                'message': '查询所有成功',
                'results': book_list
            })

    def post(self, request, *args, **kwargs):
        book_data = request.data
        if isinstance(book_data, dict) and book_data != {}:
            many = False
        elif isinstance(book_data, list):
            many = True
        else:
            return Response({
                'status': 400,
                'message': '数据格式有误……'
            })
        book_ser = BookModelSerializerV2(data=book_data, many=many)
        book_ser.is_valid(raise_exception=True)
        book_obj = book_ser.save()
        return Response({
            'status': 200,
            'message': '图书添加成功',
            'results': BookModelSerializerV2(book_obj, many=many).data
        })

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            ids = [book_id]
        else:
            ids = request.data.get('ids')

        res = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        if res:
            return Response({
                'status': status.HTTP_200_OK,
                'message': '删除成功'
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': '删除失败'
        })

    # def put(self, request, *args, **kwargs):
    #     book_data = request.data
    #     book_id = kwargs.get('id')
    #     try:
    #         book_obj = Book.objects.get(pk=book_id)
    #     except:
    #         return Response({
    #             "status": status.HTTP_400_BAD_REQUEST,
    #             "message": "图书不存在",
    #         })
    #     if not isinstance(book_data, dict) or book_data == {}:
    #         return Response({
    #             "status": 400,
    #             "message": "数据格式有误"
    #         })
    #     book_ser = BookModelSerializerV2(data=book_data, instance=book_obj)
    #     book_ser.is_valid(raise_exception=True)
    #     book_save = book_ser.save()
    #     return Response({
    #         "status": 200,
    #         "message": "更新成功",
    #         "results": BookModelSerializerV2(book_save).data
    #     })
    #
    # def patch(self, request, *args, **kwargs):
    #
    #     book_data = request.data
    #     book_id = kwargs.get('id')
    #     try:
    #         book_obj = Book.objects.get(pk=book_id)
    #     except:
    #         return Response({
    #             "status": status.HTTP_400_BAD_REQUEST,
    #             "message": "图书不存在",
    #         })
    #     if not isinstance(book_data, dict) or book_data == {}:
    #         return Response({
    #             "status": 400,
    #             "message": "数据格式有误"
    #         })
    #     book_ser = BookModelSerializerV2(data=book_data, instance=book_obj, partial=True)
    #     book_ser.is_valid(raise_exception=True)
    #     book_save = book_ser.save()
    #     return Response({
    #         "status": 200,
    #         "message": "更新成功",
    #         "results": BookModelSerializerV2(book_save).data
    #     })

    def patch(self, request, *args, **kwargs):

        book_data = request.data
        book_id = kwargs.get('id')
        if book_id and isinstance(book_data, dict):
            book_ids = [book_id]
            book_data = [book_data]
        elif not book_id and isinstance(book_data, list):
            book_ids = []
            for dic in book_data:
                pk = dic.pop('id', None)
                if pk:
                    book_ids.append(pk)
                else:
                    return Response({
                        'status': 400,
                        'message': 'id不存在'
                    })
        else:
            return Response({
                'status': 400,
                'message': '参数有误'
            })

        book_list = []
        new_data = []
        for pk in book_ids:
            try:
                book_obj = Book.objects.get(pk=pk)
                book_list.append(book_obj)
            except:
                index = book_ids.index(pk)
                book_data.pop(index)
        book_ser = BookModelSerializerV2(data=book_data, instance=book_list, partial=True, many=True)
        book_ser.is_valid(raise_exception=True)
        book_ser.save()
        return Response({
            'status': 200,
            'message': '更新成功'
        })
