from django.urls import path


from apps.plataforma.views import Dashboard
from apps.postulaciones.views import NuevaAyudantia, despliega_ofertas_ayudantias

urlpatterns = [
    # Docente
    path('nueva_ayudantia/', NuevaAyudantia.as_view(), name='nueva_ayudantia'),
    # Alumno 
    path('ofertas_ayudantias/', despliega_ofertas_ayudantias.as_view(),name= 'listar_ofertas')
]