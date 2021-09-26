from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Publicaion
from .forms import PublicacionForms
from django.contrib.auth.decorators import login_required

def publicacion_lista(request):
    publicaciones = Publicaion.objects.filter (fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/publicacion_lista.html', {'publicaciones' : publicaciones})

def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicaion, pk=pk)
    return render (request, 'blog/publicacion_detalle.html', {'publicacion' : publicacion})
'''
def publicacion_nueva(request):
    formulario = PublicacionForms()
    return render (request, 'blog/publicacion_editar.html', {'formulario' : formulario})
'''
@login_required
def publicacion_nueva(request):
    if request.method == "POST":
        formulario = PublicacionForms(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            #publicacion.fecha_publicacion = timezone.now()
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        formulario = PublicacionForms()
    return render(request, 'blog/publicacion_editar.html', {'formulario': formulario})

@login_required
def publicacion_editar(request, pk):
    publicacion = get_object_or_404(Publicaion, pk=pk)
    if request.method == "POST":
        formulario = PublicacionForms(request.POST, instance=publicacion)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            #publicacion.fecha_publicacion = timezone.now()
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        formulario = PublicacionForms(instance=publicacion)
    return render(request, 'blog/publicacion_editar.html', {'formulario': formulario})

@login_required
def publicacion_borrador_lista(request):
    publicaciones = Publicaion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/publicacion_borrador_lista.html', {'publicaciones': publicaciones})

@login_required
def publicacion_publicar(request, pk):
    publicacion = get_object_or_404(Publicaion, pk=pk)
    publicacion.publicar()
    return redirect('publicacion_detalle', pk=pk)

@login_required
def publicacion_borrar(request, pk):
    publicacion = get_object_or_404(Publicaion, pk=pk)
    publicacion.delete()
    return redirect('publicacion_lista')