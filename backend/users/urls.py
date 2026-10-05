
from django.urls import path
from .views import *

urlpatterns = [
    path('',EmployeeListCreateView.as_view(),name='employees'),
]