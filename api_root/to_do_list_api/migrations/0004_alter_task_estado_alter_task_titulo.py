# Generated by Django 5.0.6 on 2024-05-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_api', '0003_rename_tarefa_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='estado',
            field=models.CharField(choices=[('NOVA', 'Nova'), ('EM_ANDAMENTO', 'Em Andamento'), ('CONCLUIDA', 'Concluida'), ('CANCELADA', 'Cancelada')], max_length=13),
        ),
        migrations.AlterField(
            model_name='task',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]