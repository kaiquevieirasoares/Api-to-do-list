from django.db import models

class Task (models.Model):
    NOVA = "NOVA"
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"
    CANCELADA = "CANCELADA"
    
    ESTADOS = ((NOVA, 'Nova'),
               (EM_ANDAMENTO, 'Em Andamento'),
               (CONCLUIDA, 'Concluida'),
               (CANCELADA, 'Cancelada'),
               )

    id = models.AutoField(primary_key=True, unique=True)
    titulo = models.CharField(max_length=100, default='')
    descricao = models.CharField(max_length=250, blank=True)
    prazo = models.DateField()
    conclusao = models.DateField()
    estado = models.CharField(max_length=13 , choices=ESTADOS, default=NOVA)


    



