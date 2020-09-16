from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework import exceptions

from userapp.models import Book, Press


class PressModelSerializer(ModelSerializer):
    """
    出版社的序列化器
    """
    class Meta:
        model = Press
        fields = ('press_name', 'address', 'img')


class BookModelSerializer(ModelSerializer):
    """
    图书的序列化器
    """
    class Meta:
        model = Book
        fields = ('book_name', 'price', 'pic', 'publish' )
        # fields = '__all__'
        # exclude = ('is_delete', 'status')
        depth = 1


class BookModelDeSerializer(ModelSerializer):
    """
    图书的反序列化
    """
    class Meta:
        model = Book
        fields = ('book_name', 'price', 'publish', 'authors')
        extra_kwargs = {
            'book_name': {
                'max_length': 18,
                'min_length': 2,
            },
            'price': {
                'required': True,
                'decimal_places': 2,
            }
        }

    def validate(self, attrs):
        name = attrs.get('book_name')
        book = Book.objects.filter(book_name=name)
        if len(book) > 0:
            raise exceptions.ValidationError('图书名已存在')
        return attrs

    def validate_price(self, obj):
        if obj > 100:
            raise exceptions.ValidationError('图书的价格不能查过100元')
        return obj


class BookListSerializer(serializers.ListSerializer):
    """
    使用此序列化器同时修改多个对象
    """
    def update(self, instance, validated_data):
        for index, obj in enumerate(instance):
            self.child.update(obj, validated_data[index])
        return instance


class BookModelSerializerV2(ModelSerializer):
    """
    序列化器与反序列化器整合
    """
    class Meta:
        list_serializer_class = BookListSerializer
        model = Book
        fields = ('book_name', 'price', 'pic', 'publish', 'authors')
        extra_kwargs = {
            'book_name': {
                'max_length': 18,
                'min_length': 2,
            },
            'publish': {
                'write_only': True,
            },
            'authors': {
                'write_only': True,
            },
            'pic': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        name = attrs.get('book_name')
        book = Book.objects.filter(book_name=name)
        if len(book) > 0:
            raise exceptions.ValidationError('图书名已存在')
        return attrs

    def validate_price(self, obj):
        if obj > 100:
            raise exceptions.ValidationError('图书的价格不能查过100元')
        return obj