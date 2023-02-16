from django.db import models
from users.models import User


class Topico(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topico = models.ForeignKey(Topico, on_delete=models.SET_NULL, null=True)
    corpo = models.CharField(max_length=500)
    descricao = models.TextField(null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.corpo


class Resposta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE) 
    corpo = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.corpo[0:50]
