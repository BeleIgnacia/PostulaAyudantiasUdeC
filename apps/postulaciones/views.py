from django.contrib.auth import authenticate, login
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView

from apps.postulaciones.forms import RegistrarPostulacionAyudantia
from apps.plataforma.models import Curso, Usuario
from apps.postulaciones.models import Ayudantia, Postulacion
from django import forms
# Create your views here.


class  despliega_ofertas_ayudantias(ListView):
   model = Ayudantia
   template_name= 'plataforma/desplegar_ofertas_ayudantias.html'


class NuevaAyudantia(CreateView):
    model = Ayudantia
    form_class = RegistrarPostulacionAyudantia
    template_name = 'postulaciones/nueva_ayudantia.html'
    success_url = reverse_lazy('postulaciones:nueva_ayudantia')

    def get_context_data(self, **kwargs):
        context = super(NuevaAyudantia, self).get_context_data(**kwargs)
        docente = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        cursos = Curso.objects.filter(docente_id=docente)
        context['form'].fields['curso'] = forms.ModelChoiceField(queryset=cursos, 
            empty_label="Seleccione curso", widget=forms.Select(attrs={'class':'form-control'}))
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse_lazy('postulaciones:nueva_ayudantia'))
