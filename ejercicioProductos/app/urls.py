from django.urls import path, include
from . import views 

urlpatterns = [
    path("",views.indexVistaPagina),
    path("producto1/", views.producto1VistaPagina),
    path("producto2/", views.producto2VistaPagina),
    path("producto3/", views.producto3VistaPagina),
]
