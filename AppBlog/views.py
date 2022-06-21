from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import HttpResponse
from AppBlog.models import *
from django.views.generic import ListView, TemplateView
from AppBlog.forms import UserRegistrationForm, UserEditForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import *

# Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


#class Inicio(ListView):
    #def get(self, request, *args, **kwargs):
        #posts = Posts.objects.all()
        #return render(request, "AppBlog/inicio.html", {"posts": posts_list})

def inicio(request):
    posts = Posts.objects.all
    return render(request, "AppBlog/inicio.html", {"posts": posts})


def posts(request):
    return render(request, "AppBlog/posts.html", {"posts": posts})


def autores(request):
    return render(request, "AppBlog/autores.html", {"autores": autores})

def nosotras(request):

    return render(request, "AppBlog/nosotras.html")    


""" def image_upload_view(request):
    #Process images uploaded by users
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'posts.detail.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImagenForm()
    return render(request, 'posts.detail.html', {'form': form}) """

#def inicio(request):
  #avatars = Avatar.objects.filter(user=request.user.id)
  
  #return render(request, 'appBlog/inicio.html', {'url': avatars[0].avatar.url})
  # plantilla = loader.get_template('AppBlog/inicio.html')
  # documento = plantilla.render()
  # return HttpResponse(documento)    

#Acá viene el LOGIN Y REGISTRO    

def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data = request.POST)
    
    if form.is_valid():
      usuario = form.cleaned_data.get('username')
      clave = form.cleaned_data.get('password')
      
      # Autenticación de usuario
      user = authenticate(username=usuario, password=clave) # Si este usuario existe me lo trae
     
      if user is not None:
        login(request,user) # Si existe, lo loguea
        return render(request, 'AppBlog/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
      else:
        return render(request, 'AppBlog/inicio.html', {'mensaje': 'Error, datos incorrectos'})
    else:
        return render(request,'AppBlog/inicio.html', {'mensaje': 'Error, formulario erróneo'})
  
  form = AuthenticationForm() # Creo un formulario vacío si vengo por GET
  return render(request, 'AppBlog/login.html', {'form':form})

def registro(request):
  if request.method == 'POST': # Si es POST, entonces es un formulario que viene lleno
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      return render(request, 'AppBlog/inicio.html', {'mensaje': f'Usuario {username} creado correctamente'})
    else:
      return render(request, 'AppBlog/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario'})
  else:
    form = UserRegistrationForm()
    return render(request, 'AppBlog/registro.html', {'form': form})

@login_required
def editarPerfil(request):
  usuario = request.user

  if request.method == 'POST':
    formulario = UserEditForm(request.POST, instance=usuario)
    if formulario.is_valid():
      informacion = formulario.cleaned_data

      usuario.email = informacion['email']
      usuario.password1 = informacion['password1']
      usuario.password2 = informacion['password2']
      usuario.save()

      return render(request, 'AppBlog/inicio.html', {'usuario': usuario, 'mensaje': 'Datos actualizados correctamente'})
  else:
    formulario = UserEditForm(initial={'email':usuario.email})
  return render(request, 'AppBlog/editarPerfil.html', {'formulario': formulario, 'usuario': usuario.username}) 

  #CRUD

  
class PostsList(ListView):

    model = Posts
    template_name = "AppBlog/posts_list.html"

class PostDetail(DetailView):

    model = Posts
    template_name = "AppBlog/posts_detail.html"


class PostCreate(CreateView):

    model = Posts
    success_url = reverse_lazy('posts_lista') # Redirecciono a la vista de posts luego de crear un post
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']


class PostUpdate(UpdateView):

    model = Posts
    success_url = reverse_lazy('posts_lista')
    fields = ['titulo', 'subtitulo', 'cuerpo']

class PostDelete(DeleteView):

    model = Posts
    success_url = reverse_lazy('posts_lista')


class AutoresList(ListView):

    model = Autores
    template_name = "AppBlog/autores_list.html"

class AutoresDetail(DetailView):

    model = Autores
    template_name = "AppBlog/autores_detail.html"

class AutoresCreate(CreateView):

    model = Autores
    success_url = reverse_lazy('autores_lista') # Redirecciono a la vista de autores luego de crear un autor
    fields = ['nombre', 'apellido', 'email', 'imagen']

class AutoresUpdate(UpdateView):

    model = Autores
    success_url = reverse_lazy('autores_lista')
    fields = ['nombre', 'apellido', 'email']

class AutoresDelete(DeleteView):

    model = Autores
    success_url = reverse_lazy('autores_lista')    