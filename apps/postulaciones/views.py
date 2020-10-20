from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from apps.postulaciones.models import Ayudantia
from apps.plataforma.models import Curso

# Create your views here.
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