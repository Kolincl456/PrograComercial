from typing import ValuesView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.publicacion_lista, name='publicacion_lista'),
]
