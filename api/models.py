from django.db import models

class Aluno(models.Model):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    data_ingresso = models.DateField()
        