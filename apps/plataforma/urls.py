from django.urls import path

from apps.plataforma.views import Dashboard, RegistrarDocente, NuevoCurso

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    # Administrador
    path('nuevo_docente/', RegistrarDocente.as_view(), name='registrar_docente'),
    # Docente
    path('nuevo_curso/', NuevoCurso.as_view(), name='nuevo_curso')
    # Alumno
]
