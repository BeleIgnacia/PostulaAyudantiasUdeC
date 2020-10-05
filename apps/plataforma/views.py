from django.shortcuts import render
from django.views.generic import CreateView


class RegistrarAlumno(CreateView):
    template_name = 'plataforma/register_alumno.html'


def iniciar_sesion(request):
    pass
