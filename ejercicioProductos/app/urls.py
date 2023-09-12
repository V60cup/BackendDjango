from django.urls import path, include
from . import views 

urlpatterns = [
    path("",views.indexVistaPagina, name="inicio"),
    path("cafegrano/", views.producto1VistaPagina, name="cafegrano"),
    path("accesorios/", views.producto2VistaPagina, name="accesorios"),
    path("cursos/", views.producto3VistaPagina, name="cursos"),
]
