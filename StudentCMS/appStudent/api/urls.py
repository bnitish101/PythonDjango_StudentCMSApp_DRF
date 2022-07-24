from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListAPIView.as_view(), name="index"),
    path('add/', views.StudentCreateAPIView.as_view(), name="add"),
    
    path('<int:pk>/', views.StudentRetrieveAPIView.as_view(), name="detail"),
    path('<int:pk>/delete', views.StudentDestroyAPIView.as_view(), name="delete"),
    path('<int:pk>/update', views.StudentUpdateAPIView.as_view(), name="update"),
    
    #CRUD - Create, Read, Update, Delete
    path('cr/', views.StudentListCreateAPIView.as_view(), name="cr"),
    path('ru/<int:pk>', views.StudentRetrieveUpdateAPIView.as_view(), name="cr"),
    path('rd/<int:pk>', views.StudentRetrieveDestroyAPIView.as_view(), name="rd"),
    path('rud/<int:pk>', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name="rud"),
]