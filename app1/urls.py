from django.urls import path
from app1.views import *
app_name='ravi'

urlpatterns=[
    path('bala/',bala,name='bala'),
]