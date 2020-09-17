from django.urls import path

from studentapp import views

urlpatterns = [
    path('stu_gen/', views.StudentGenericAPIView.as_view()),
    path('stu_gen/<str:id>/', views.StudentGenericAPIView.as_view()),
    path('stu_mix/', views.StudentGenericMixinView.as_view()),
    path('stu_mix/<str:id>/', views.StudentGenericMixinView.as_view()),
    path('stu_set/', views.StudentModelViewSet.as_view({'post': 'user_login', 'get': 'update_all'})),
    path('stu_set/', views.StudentModelViewSet.as_view({'post': 'user_register'})),
    path('stu_set/<str:id>/', views.StudentModelViewSet.as_view({'post': 'user_login', 'get': 'update_all'})),
]