from django.contrib.auth import authenticate, login
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, ListView
from apps.plataforma.models import Curso
from apps.postulaciones.models import Ayudantia, Postulacion
# Create your views here.


class  despliega_ofertas_ayudantias(ListView):
   model = Ayudantia
   template_name= 'plataforma/desplegar_ofertas_ayudantias.html'


class NuevaAyudantia(TemplateView): #Cambiar a CreateView cuando se tenga form
    model = Ayudantia
    #form class = NuevaAyudantiaForm
    template_name = 'postulaciones/nueva_ayudantia.html'
    #success_url = reverse_lazy('postulaciones:nueva_ayudantia')

    #def get_context_data(self, **kwargs):
    #    context = super(NuevaAyudantia, self).get_context_data(**kwargs)
    #    if 'form' not in context:
    #        context['form'] = self.form_class(self.request.GET)
    #    return context
    
    #def form_valid(self, form):
    #    instance = form.save(commit=False)
    #    curso = 
    #    instance.curso = curso
    #    instance.save()
    #    return HttpResponseRedirect(success_url)
