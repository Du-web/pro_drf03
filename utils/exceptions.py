from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status


def exception_handler(exc, context):
    error = f'{context["view"]}{context["request"].method}{exc}'
    print(error)
    response = drf_exception_handler(exc, context)
    if response is None:
        return Response(
            {'error_message': '请稍等，正在飞速处理中……'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            exception=None
        )
    return response