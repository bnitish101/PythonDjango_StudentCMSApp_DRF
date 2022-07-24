from django.contrib import admin
from django.urls import path, include
# from .api import views
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('appStudent.api.urls')),
]