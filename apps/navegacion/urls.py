from django.urls import path

from apps.navegacion.views import Inicio, Ayuda, Contacto

urlpatterns = [
    path('', Inicio.as_view()),
    path('ayuda/', Ayuda.as_view()),
    path('contacto/', Contacto.as_view()),
]
