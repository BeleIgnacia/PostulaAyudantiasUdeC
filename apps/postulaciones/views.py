from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin

from apps.postulaciones.forms import RegistrarPostulacionAyudantia,RegistrarPostulacionAlumno
from apps.plataforma.models import Curso, Usuario
from apps.postulaciones.models import Ayudantia, Postulacion
from django import forms


class OfertasAyudantias(LoginRequiredMixin, ListView):
    login_url = '/iniciar/'
    model = Postulacion
    form_class = RegistrarPostulacionAlumno
    template_name = 'plataforma/desplegar_ofertas_ayudantias.html'

    # Filtra las ayudantias a las cuales ya he postulado
    def get_queryset(self):
        alumno = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        postulaciones = Postulacion.objects.filter(alumno=alumno)
        return Ayudantia.objects.exclude(postulacion__in=postulaciones)

   
        return HttpResponseRedirect(reverse_lazy('postulaciones:listar_ofertas'))
    
    def post(self, request, *args, **kwargs):
        id_ayudantia = request.POST.get('id_ayudantia')
        semestreramo = request.POST.get('semestre')
        nota = request.POST.get('nota')
        ayudantia = Ayudantia.objects.get(pk=id_ayudantia)
        alumno = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        Postulacion.objects.create(
            alumno=alumno,
            ayudantia=ayudantia,
            semestreramo=semestreramo,
            nota = nota
        )
        return HttpResponseRedirect(reverse_lazy('postulaciones:listar_ofertas'))

class NuevaPostulacion(UserPassesTestMixin, CreateView):
    login_url = '/iniciar/'  # Redirecciona en caso de no haber iniciado sesión
    model = Postulacion
    form_class = RegistrarPostulacionAlumno
    template_name = 'postulaciones/generar_postulacion.html'
    success_url = reverse_lazy('postulaciones:generar_postulacion')

    def test_func(self):
        return not(self.request.session.get('es_docente'))
    
      
      # Crea una postualción sobre la ayudantía escogida
    
    
    




class NuevaAyudantia(UserPassesTestMixin, CreateView):
    login_url = '/iniciar/'  # Redirecciona en caso de no haber iniciado sesión
    model = Ayudantia
    form_class = RegistrarPostulacionAyudantia
    template_name = 'postulaciones/nueva_ayudantia.html'
    success_url = reverse_lazy('postulaciones:nueva_ayudantia')

    # Comprueba que el usuario accediendo es docente
    def test_func(self):
        return self.request.session.get('es_docente')

    def get_context_data(self, **kwargs):
        context = super(NuevaAyudantia, self).get_context_data(**kwargs)
        docente = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        cursos = Curso.objects.filter(docente_id=docente)
        context['form'].fields['curso'] = forms.ModelChoiceField(queryset=cursos, empty_label="Seleccione curso", widget=forms.Select(attrs={'class': 'form-control'}))
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


# Postulaciones realizadas sobre mis ayudantias ofrecidas
class PostulacionesRealizadas(ListView):
    model = Postulacion
    template_name = 'postulaciones/postulaciones_realizadas.html'

    # Filtra las postulaciones sobre mis ayudantias
    def get_queryset(self):
        docente = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        ayudantias = Ayudantia.objects.filter(curso__docente=docente)
        return Postulacion.objects.filter(ayudantia__in=ayudantias)
