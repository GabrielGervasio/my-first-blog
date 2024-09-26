from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
 
    def __str__(self):
        return self.username




class Atletica(models.Model):
    nome = models.CharField(max_length=100)
    membros = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='atletica_membros')
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='atletica_fotos/', null=True, blank=True)

    def __str__(self):
        return self.nome



class Palestra(models.Model):
    nome = models.CharField(max_length=200)
    tema = models.CharField(max_length=200)
    area_de_estudo = models.CharField(max_length=100)
    descricao = models.TextField()
    palestrante = models.CharField(max_length=100)  # campo para o nome do palestrante
    data_hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    membros = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='equipe_membros')
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='equipe_fotos/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title