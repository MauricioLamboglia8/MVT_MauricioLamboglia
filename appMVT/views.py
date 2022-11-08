from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from appMVT.models import Familiar


def vista_listado_familiares(request):
    
    listado_datos = ['Roberto Lamboglia', 'Edad: 75', 'Nacido en: ARG', 'Fecha de nacimiento: 14/07/47']

    datos = {'familiar': 'Padre', 'listado_datos': listado_datos}
    
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)

def vista_listado_familiares2(request):
    
    listado_datos = ['Mariana Lamboglia', 'Edad: 37', 'Nacida en: ARG', 'Fecha de nacimiento: 23/04/1985']

    datos = {'familiar': 'Hermana', 'listado_datos': listado_datos}
    
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)

def vista_listado_familiares3(request):
    
    listado_datos = ['Adrian Lamboglia', 'Edad: 42', 'Nacido en: ARG', 'Fecha de nacimiento: 02/06/1980']

    datos = {'familiar': 'Hermano', 'listado_datos': listado_datos}
    
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)