from django.contrib import admin
from django.urls import  path

from .views import (ListTasksView, CreateTaskView, RetrieveTaskView, UpdateTaskView,DeletedTaskView)
urlpatterns = [
    path('tasks/', ListTasksView.as_view(), name='get-all'),
    path('tasks/create/', CreateTaskView.as_view(), name='create'),
    path('tasks/get/<pk>/', RetrieveTaskView.as_view(), name='get-by-id'),
    path('tasks/update/<pk>/', UpdateTaskView.as_view(), name='update'),
    path('tasks/delete/<pk>/', DeletedTaskView.as_view(), name='delete'),
]
