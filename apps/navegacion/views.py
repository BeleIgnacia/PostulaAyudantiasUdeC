from django.shortcuts import render

from django.views.generic import View, TemplateView


class Inicio(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'plataforma/dashboard.html')
        else:
            return render(request, 'navegacion/inicio.html')


class Nosotros(TemplateView):
    template_name = 'navegacion/nosotros.html'


class Ayuda(TemplateView):
    template_name = 'navegacion/ayuda.html'


class Contacto(TemplateView):
    template_name = 'navegacion/contacto.html'
