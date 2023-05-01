from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory

from personas.models import Persona


# Create your views here.
def detallePersona(request, id):
    # Recuperamos la persona mediante el id de nuestra BBDD
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
