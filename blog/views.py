from django.shortcuts import render

from .models import Publicacion

def publicacion_lista(request):
    return render(request, 'blog/publicacion_lista.html', {})