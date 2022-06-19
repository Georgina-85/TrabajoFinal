from django.urls import path
from AppBlog import views
from AppBlog.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',Inicio.as_view(), name = 'inicio'),
  path('posts/', PostsList.as_view(), name='posts_lista'),
  path('posts/<pk>', PostDetail.as_view(), name='posts_detalle'),
  path('posts/editar/<pk>', PostUpdate.as_view(), name='posts_editar'),
  path('posts/nuevo/', PostCreate.as_view(), name='posts_crear'),
  path('posts/borrar/<pk>', PostDelete.as_view(), name='posts_borrar'),

  path('autores/', AutoresList.as_view(), name = 'autores_lista'),
  path('autores/<pk>', AutoresDetail.as_view(), name='autores_detalle'),
  path('autores/editar/<pk>', AutoresUpdate.as_view(), name='autores_editar'),
  path('autores/nuevo/', AutoresCreate.as_view(), name='autores_crear'),
  path('autores/borrar/<pk>', AutoresDelete.as_view(), name='autores_borrar'),

  path('nosotras/',views.nosotras, name = 'nosotras'),

  path('login', login_request, name = "Login"),
  path('registro', registro, name = "Registro"),
  #path('logout', LogoutView.as_view(), name = "Logout"),

  path('editarPerfil', editarPerfil, name = "editarPerfil"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

   

