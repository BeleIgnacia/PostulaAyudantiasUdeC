from django.urls import path

from apps.plataforma.views import Dashboard, RegistrarDocente

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    # Administrador
    path('nuevo_docente/', RegistrarDocente.as_view(), name='registrar_docente'),
    # Docente
    # Alumno
]
