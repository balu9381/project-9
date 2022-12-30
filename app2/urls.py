from django.urls import path
from app2.views import *
app_name='balu'

urlpatterns=[
    path('balu/',balu,name='balu'),
]