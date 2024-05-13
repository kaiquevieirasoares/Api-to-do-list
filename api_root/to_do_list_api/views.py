from rest_framework.generics import ( 
    ListAPIView,
    RetrieveAPIView, 
    CreateAPIView,
    DestroyAPIView, 
    UpdateAPIView
    
    )

from .models import Task
from .serializers import (TaskSerializer )

class ListTasksView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTaskView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

