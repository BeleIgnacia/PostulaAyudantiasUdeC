from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import View, TemplateView


class Inicio(View):
    def get(self, request):
        if request.user.is_authenticated:
            if self.request.session.get('es_docente', ''):
                return HttpResponseRedirect(reverse('postulaciones:mis_ayudantias'))
            else:
                return HttpResponseRedirect(reverse('postulaciones:listar_ofertas'))
        else:
            return render(request, 'navegacion/inicio.html')


class Nosotros(TemplateView):
    template_name = 'navegacion/nosotros.html'


class Ayuda(TemplateView):
    template_name = 'navegacion/ayuda.html'


class Contacto(TemplateView):
    template_name = 'navegacion/contacto.html'
