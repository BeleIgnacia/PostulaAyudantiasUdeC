from django.contrib import admin
from django.urls import path, include

from apps.plataforma.views import RegistrarAlumno, iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('admin/', admin.site.urls),
    # El primer argumento de path es un prefijo para la url
    # dentro del include se añaden las urls que tiene la app y se le da un namespace
    # el namespace se utiliza por lo regular dentro de las views para referenciar una url
    # al realizar un redirect
    # por ejemplo. navegacion:inicio o navegacion:ayuda
    path('', include(('apps.navegacion.urls', 'app_name'), namespace='navegacion')),
    path('plataforma/', include(('apps.plataforma.urls', 'app_name'), namespace='plataforma')),
    path('postulaciones/', include(('apps.postulaciones.urls', 'app_name'), namespace='postulaciones')),
    # Entradas de registro e inicio de sesión
    path('registro/', RegistrarAlumno.as_view(), name='register_alumno'),
    path('iniciar/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar/', cerrar_sesion, name='cerrar_sesion'),
]
