from django.urls import path
from . import views

urlpatterns = [
    path('', views.refinance, name='refinance'),
    path('refinancecalc', views.refinancecalc, name='refinancecalc'),
]
