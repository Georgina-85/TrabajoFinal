from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = RichTextField()
    autor = models.CharField(max_length=40)
    fecha = models.DateField(default=datetime.now)
    imagen = models.URLField(max_length = 255, blank = False, null= False)

    class Meta:
        verbose_name_plural = "Posts"
        verbose_name = "Post"

    def __str__(self):
        return f'{self.titulo} by {self.autor}'

class Autores(models.Model):
    nombre = models.CharField(max_length=40)  
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    imagen = models.URLField(max_length = 255, blank = False, null= False)
    
    class Meta:
        verbose_name_plural = "Autores"
        verbose_name = "Autor"

    def __str__(self): 
        return f"{self.nombre}  {self.apellido} - {self.email}"   


""" class Imagen(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='pictures')

    class Meta:
        verbose_name_plural = "Imagenes"
        verbose_name = "Imagen"

    def __str__(self):
        return f"{self.title}"          """   

class Avatar(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to='avatars', blank=True, null=True)    

  class Meta:
        verbose_name_plural = "Avatar"
        verbose_name = "Avatar"

  def __str__(self): 
        return f"{self.user}  {self.avatar}"   