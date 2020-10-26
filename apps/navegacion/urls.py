from django.urls import path

from apps.navegacion.views import Inicio, Ayuda, Contacto, Nosotros

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('nosotros/', Nosotros.as_view()),
    path('ayuda/', Ayuda.as_view()),
    path('contacto/', Contacto.as_view()),
]
