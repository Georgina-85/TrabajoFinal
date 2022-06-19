from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.TextField('Descripción')
    autor = models.CharField(max_length=40)
    fecha = models.DateField(default=datetime.now)
    imagen = models.ImageField(upload_to='pictures', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Posts"
        verbose_name = "Post"

    def __str__(self):
        return f'{self.titulo} by {self.autor}'

class Autores(models.Model):
    nombre = models.CharField(max_length=40)  
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    imagen = models.ImageField(upload_to='pictures', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Autores"
        verbose_name = "Autor"

    def __str__(self): 
        return f"{self.nombre}  {self.apellido} - {self.email}"        

class Avatar(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to='avatars', blank=True, null=True)        