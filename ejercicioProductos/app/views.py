from django.shortcuts import render
from django.http import HttpResponse

def indexVistaPagina(request):
    return HttpResponse("Pagina Principal")

def producto1VistaPagina(request):
    return HttpResponse("Producto 1")

def producto2VistaPagina(request):
    return HttpResponse("Producto 2")

def producto3VistaPagina(request):
    return render(request, "index.html")