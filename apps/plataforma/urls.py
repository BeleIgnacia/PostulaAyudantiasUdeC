from django.urls import path

from apps.plataforma.views import Dashboard, ActualizarPerfil, MisCursos

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('perfil/<pk>/', ActualizarPerfil.as_view(), name='perfil'),
    # Administrador
    # path('nuevo_docente/', RegistrarDocente.as_view(), name='registrar_docente'),
    # Docente
    # path('nuevo_curso/', NuevoCurso.as_view(), name='nuevo_curso'),
    path('mis_cursos/', MisCursos.as_view(), name='mis_cursos')
    # Alumno
]
