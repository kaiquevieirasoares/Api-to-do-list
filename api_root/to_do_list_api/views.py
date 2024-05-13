from rest_framework.generics import ( 
    ListAPIView,
    RetrieveAPIView, 
    CreateAPIView,
    DestroyAPIView, 
    UpdateAPIView
    
    )

from .models import Task
from .serializers import (TaskSerializer )

# Get
class ListTasksView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Post
class CreateTaskView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Get by id

class RetrieveTaskView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Put
class UpdateTaskView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#Delete
class DeletedTaskView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    

