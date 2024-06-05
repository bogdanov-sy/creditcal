from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='insurance'),
    path('calculatecredit', views.calculate, name='calculatecredit'),
    path('download/<str:filename>/', views.download_file, name='download_file'),
]
