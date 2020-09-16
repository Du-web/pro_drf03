from django.urls import path

from studentapp import views

urlpatterns = [
    path('stu_gen/', views.StudentGennericAPIView.as_view()),
]