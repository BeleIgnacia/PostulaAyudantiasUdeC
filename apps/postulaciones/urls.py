from django.urls import path

from apps.plataforma.views import Dashboard
from apps.postulaciones.views import NuevaAyudantia

urlpatterns = [
    # Docente
    path('nueva_ayudantia/', NuevaAyudantia.as_view(), name='nueva_ayudantia')
]