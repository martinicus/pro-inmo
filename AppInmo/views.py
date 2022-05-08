from django.http import HttpResponse
from django.shortcuts import render
from AppInmo.models import *


# Create your views here

def inicio(request):
    return render(request, "AppInmo/inicio.html")

def alquiler(request):
    return render(request, "AppInmo/alquiler.html")

def compra(request):
    return render(request, "AppInmo/compra.html")

def venta(request):
    return render(request, "AppInmo/venta.html")

def alquilerFormulario(request):
    if request.method=="POST":
        print(request.POST)

    return render(request, "AppInmo/alquilerformulario.html")

