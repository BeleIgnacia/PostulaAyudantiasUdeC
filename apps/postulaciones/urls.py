from django.urls import path

from apps.plataforma.views import Dashboard
from apps.postulaciones.views import NuevaAyudantia, OfertasAyudantias, PostulacionesRealizadas

urlpatterns = [
    # Docente
    path('nueva_ayudantia/', NuevaAyudantia.as_view(), name='nueva_ayudantia'),
    path('mis_ayudantias/', PostulacionesRealizadas.as_view(), name='mis_ayudantias'),
    # Alumno 
    path('ofertas_ayudantias/', OfertasAyudantias.as_view(), name='listar_ofertas')
]
