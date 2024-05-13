from rest_framework.generics import ( 
    ListAPIView,
    RetrieveAPIView, 
    CreateAPIView,
    DestroyAPIView, 
    UpdateAPIView
    
    )

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Task
from .serializers import (TaskSerializer )



# Get
class ListTasksView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#Search 
class SearchTaskView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'descricao']


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


    

