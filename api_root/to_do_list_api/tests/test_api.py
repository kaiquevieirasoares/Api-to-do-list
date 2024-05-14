from django.urls import reverse, resolve
from django.test import SimpleTestCase
from rest_framework.test import (APITestCase)
from ..views import ListTasksView
from rest_framework import status



class APiTestUrlsTests(SimpleTestCase):

    def test_the_same_url(self):
        url = reverse('get-all')
        print(resolve(url).func.view_class, ListTasksView)

class TaskApiViewTests(APITestCase):
    list_task_view_url = reverse('get-all')

    def test_get_all_tasks(self):
        response = self.client.get(self.list_task_view_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
