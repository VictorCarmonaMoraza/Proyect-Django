from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
    #Creacion del diccionario
    mensajes ={
        'clave1':'Valor mensaje 1',
         'clave2':'Valor mensaje 2'
    }
    #Responderemos de momento con un Hola mundo
    return render(request,'bienvenido.html', mensajes)

#Metodo de despedia
def despedirse(request):
    return HttpResponse('Despedida desde Django')

#Metodo para mostrar info del contacto
def contacto(request):
    return HttpResponse('Para mas info, llamar al numero 421542 y le atendera Pedro')