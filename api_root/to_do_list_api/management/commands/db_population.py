from django.core.management import BaseCommand, CommandError
from django.core.management.base import CommandParser
from ...models import Task
import json

directory_url = ("../api_root/to_do_list_api/management/Files/tasks_data.json")

with open(directory_url) as data:
    data_json = json.load(data)

class Command(BaseCommand):
    help = "Esse Script instancia 15 tarefas (Tasks) no Banco de Dados."

    
    def handle(self, *arg, **options):
        for i in range(len(data_json)):
            Task.objects.create(titulo = data_json[i]['titulo'],
                                descricao = data_json[i]['descricao'],
                                prazo = data_json[i]['prazo'],
                                conclusao = data_json[i]['conclusao'],
                                estado = data_json[i]['estado']
                                )
            
        print("\033[32mThis script ran correctly!\033[32m")
        

        
        