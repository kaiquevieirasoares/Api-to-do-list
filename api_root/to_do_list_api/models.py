from django.db import models

class Task (models.Model):
    NOVA = 1
    EM_ANDAMENTO = 2
    CONCLUIDA = 3
    CANCELADA = 4
    
    ESTADOS = ((NOVA, 'Nova'),
               (EM_ANDAMENTO, 'Em Andamento'),
               (CONCLUIDA, 'Concluida'),
               (CANCELADA, 'Cancelada'),
               )

    id = models.AutoField(primary_key=True, unique=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250, blank=True)
    prazo = models.DateField()
    conclusao = models.DateField()
    estado = models.IntegerField(max_length=1, choices=ESTADOS)

    def __str__(self) -> str:
        return self.titulo

    



