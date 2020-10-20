from django.contrib.auth import authenticate, login
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, ListView


from apps.postulaciones.models import Ayudantia, Postulacion
# Create your views here.


class  despliega_ofertas_ayudantias(ListView ):
   model = Ayudantia
   template_name= 'plataforma/desplegar_ofertas_ayudantias.html'


