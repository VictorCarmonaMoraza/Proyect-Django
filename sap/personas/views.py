from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == 'POST':
        #Rellenamos el objeto perosna con la data obtenida del formulario. Con esto ya tenemos toda la informacion
        # en nuestro objeto persona
        formaPersona = PersonaForm(request.POST)
        #Validamos el formulario
        if formaPersona.is_valid():
            #Insertamos en la BBDD
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})