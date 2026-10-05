
from django.urls import path
from .views import *

urlpatterns = [
    path('',EmployeeListView.as_view(),name='employee-list')
]