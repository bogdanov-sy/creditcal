from django.urls import path
from . import views

urlpatterns = [
    path('', views.insurance, name='insurance'),
    path('calculatecredit' ,views.calculatecredit, name='calculatecredit')
]
