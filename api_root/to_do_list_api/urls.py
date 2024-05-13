from django.contrib import admin
from django.urls import  path

from .views import (ListTasksView, CreateTaskView)
urlpatterns = [
    path('tasks/', ListTasksView.as_view(), name='get-all-tasks'),
    path('tasks/create/', CreateTaskView.as_view(), name='create'),
]
