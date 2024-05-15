from django.test import TestCase
from django.urls import reverse
from ..models import Task


class APiTestUrlsTests(TestCase):

    def set_up_data_base_for_teste(cls):
        number_of_tasks = 15
        for task in range(number_of_tasks):
            Task.objects.create(
                titulo = 'fazer as compras',
                descricao = 'descricao',
                prazo = '2005-10-10',
                conclusao = '2005-10-11',
                estado = 1
                )
    
    def test_url_get_is_ok(self):
        response_put = self.client.put(reverse('get-all'))
        response_patch = self.client.patch(reverse('get-all'))
        response_delete = self.client.delete(reverse('get-all'))
        response_post = self.client.post(reverse('get-all'))
        self.assertEqual(response_put.status_code, 405)
        self.assertEqual(response_patch.status_code, 405)
        self.assertEqual(response_post.status_code, 405)    
        self.assertEqual(response_delete.status_code, 405)

    
    def test_create_url_task_is_ok(self):
        response = self.client.post(reverse('create'))
        self.assertEqual(response.status_code, 400)
    
    def test_create_url_task_is_ok(self):
        response_get = self.client.get(reverse('create'))
        response_put = self.client.put(reverse('create'))
        response_patch = self.client.patch(reverse('create'))
        response_delete = self.client.delete(reverse('create'))
        self.assertEqual(response_put.status_code, 405)
        self.assertEqual(response_get.status_code, 405)
        self.assertEqual(response_patch.status_code, 405)
        self.assertEqual(response_delete.status_code, 405)
    
    def test_search_is_return_status_code_correct(self):
        response_post = self.client.post(reverse('search'))
        response_delete = self.client.delete(reverse('search'))
        response_patch = self.client.patch(reverse('search'))
        response_put= self.client.put(reverse('search'))
        self.assertEqual(response_patch.status_code, 405)
        self.assertEqual(response_post.status_code, 405)
        self.assertEqual(response_delete.status_code, 405)
        self.assertEqual(response_put.status_code, 405)

    def test_delete_is_return_status_code_correct(self):
        response_get = self.client.get('/api/v1/tasks/delete/1/')
        response_post = self.client.post(('/api/v1/tasks/delete/1/'))
        response_patch = self.client.patch(('/api/v1/tasks/delete/1/'))
        response_put= self.client.put(('/api/v1/tasks/delete/1/'))
        self.assertEqual(response_get.status_code, 405)
        self.assertEqual(response_patch.status_code, 405)
        self.assertEqual(response_post.status_code, 405)    
        self.assertEqual(response_put.status_code, 405)
