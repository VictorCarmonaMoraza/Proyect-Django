from django.shortcuts import render
from django.http import HttpResponse

from personas.models import Persona

# Create your views here.
def bienvenido(request):
    #Utilizamos nuestro modelo de Persona
     numero_personas = Persona.objects.count()
     return render(request, 'bienvenido.html', {'numero_personas':numero_personas})
