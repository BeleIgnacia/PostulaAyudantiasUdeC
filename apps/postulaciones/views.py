from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from django.contrib import messages

from apps.postulaciones.forms import RegistrarPostulacionAyudantia
from apps.plataforma.models import Curso, Usuario
from apps.postulaciones.models import Ayudantia, Postulacion
from django import forms
# Create your views here.


class  despliega_ofertas_ayudantias(LoginRequiredMixin, ListView):
   login_url = '/iniciar/'
   model = Ayudantia
   template_name= 'plataforma/desplegar_ofertas_ayudantias.html'


class NuevaAyudantia(UserPassesTestMixin, CreateView):
    login_url = '/iniciar/' #Redirecciona en caso de no haber iniciado sesión
    model = Ayudantia
    form_class = RegistrarPostulacionAyudantia
    template_name = 'postulaciones/nueva_ayudantia.html'
    success_url = reverse_lazy('postulaciones:nueva_ayudantia')

    #Comprueba que el usuario accediendo es docente
    def test_func(self):
        return self.request.session.get('es_docente')

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

        cursos_ids = Ayudantia.objects.values_list('curso_id', flat=True)
        cursos = Curso.objects.filter(id__in=cursos_ids)
        for curso in cursos:
            if instance.curso.codigo == curso.codigo:
                messages.error(self.request, "Ya existe una ayudantía para este curso.")
                return HttpResponseRedirect(self.request.path_info) 

        instance.save()
        return HttpResponseRedirect(reverse_lazy('postulaciones:nueva_ayudantia'))
