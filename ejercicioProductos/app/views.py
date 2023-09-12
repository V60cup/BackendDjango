from django.shortcuts import render
from django.http import HttpResponse

def indexVistaPagina(request):
     return render(request, "index.html")

def producto1VistaPagina(request):
    return render(request, "cafeGrano.html")

def producto2VistaPagina(request):
     return render(request, "accesoriosBarista.html")

def producto3VistaPagina(request):
    return render(request, "cursosBarismo.html")