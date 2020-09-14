from django.urls import path

from userapp import views

urlpatterns = [
    path('user/', views.EmployeeAPIView.as_view()),
    path('user/<str:id>/', views.EmployeeAPIView.as_view()),
]