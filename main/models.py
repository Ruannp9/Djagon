from django.db import models

# Create your models here.

class Aluno(models.Model):
    
    nome= models.CharField(max_length=225)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField(null=True)
    descripton = models.TextField()
    
    def __str__(self):
        return self.nome
