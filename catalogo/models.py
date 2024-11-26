from django.db import models
from django.core.validators import FileExtensionValidator

class Catalogo(models.Model):
    titulo = models.CharField(max_length=100)
    elenco = models.CharField(max_length=100)
    genero = models.CharField(max_length=20)
    capa = models.ImageField(upload_to='capas/', validators= [FileExtensionValidator(['png','jpg','jpeg'])])

    def __str__(self):
        return f"{self.titulo} {self.elenco}"

class Filme(models.Model):
    nome = models.CharField(max_length=25)
    filme = models.ManyToManyField(Catalogo)

    def __str__(self):
        return self.nome
                             
                             
# Create your models here.
