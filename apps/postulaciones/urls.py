from django.urls import path

from apps.postulaciones.views import NuevaAyudantia, OfertasAyudantias, PostulacionesRealizadas, PostulacionesAlumno

urlpatterns = [
    # Docente
    path('nueva_ayudantia/', NuevaAyudantia.as_view(), name='nueva_ayudantia'),
    path('mis_ayudantias/', PostulacionesRealizadas.as_view(), name='mis_ayudantias'),
    # path('mis_ayudantias/', MisCursos.as_view(), name='mis_cursos'),
    # Alumno 
    path('mis_postulaciones/', PostulacionesAlumno.as_view(), name='mis_postulaciones'),
    path('ofertas_ayudantias/', OfertasAyudantias.as_view(), name='listar_ofertas'),
    path('ofertas_ayudantias/<str:order>/', OfertasAyudantias.as_view()),
    path('ofertas_ayudantias/<str:search>/', OfertasAyudantias.as_view())
]
