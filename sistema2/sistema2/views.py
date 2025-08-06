from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime

lista = [45, 30, 200]
def consultar(request, num):
    if num in lista:
        mensaje = "El No. existe en las lista"
    else:
        mensaje = "El No. no existe es las lista"

    return HttpResponse(mensaje)

def fechaHora(request):
    now = datetime.datetime.now()
    html = "<h1>Hoy es %s.</h1>" % now
    return HttpResponse(html)

def plantillaIndex(request):
    #cargador de plantilla> loader
    plantilla = loader.get_template('index.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def plantillaLogin(request):
    return render(request, 'login.html')
    