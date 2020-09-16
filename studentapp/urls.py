from django.urls import path

from studentapp import views

urlpatterns = [
    path('stu_gen/', views.StudentGenericAPIView.as_view()),
    path('stu_gen/<str:id>/', views.StudentGenericAPIView.as_view()),
]