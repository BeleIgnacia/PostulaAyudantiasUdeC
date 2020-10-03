from django.shortcuts import render

from django.views.generic import TemplateView


class Inicio(TemplateView):
    template_name = 'navegacion/inicio.html'


class Ayuda(TemplateView):
    template_name = 'navegacion/ayuda.html'


class Contacto(TemplateView):
    template_name = 'navegacion/contacto.html'
