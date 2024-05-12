from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer

import json

@api_view(['GET'])
def get_task(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def get_task_filter(request):


