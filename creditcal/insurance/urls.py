from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='insurance'),
    path('calculatecredit', views.calculate, name='calculatecredit'),
]
