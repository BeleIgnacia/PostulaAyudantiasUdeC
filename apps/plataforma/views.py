from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.plataforma.forms import RegistrarAlumnoForm
from apps.plataforma.models import Usuario


# Esta es una vista para creación de un modelo
# por eso hereda de CreateView
class RegistrarAlumno(CreateView):
    # Se define el modelo sobre el que añade una instancia
    model = Usuario
    # El formulario que se despliega dentro de la vista
    form_class = RegistrarAlumnoForm
    # El html que se muestra en el navegador
    template_name = 'plataforma/register_alumno.html'
    # La dirección en caso de que el formulario sea correcto
    # aquí se utiliza namespace:name
    success_url = reverse_lazy('plataforma:inciar')

    ''' Las dos funciones de aquí abajo se repiten por lo regular
    en todas las views. Existen otras maneras de manjar los eventos
    con otras funciones pero estas por lo regular son suficientes '''

    # Función que se ejecuta antes de entregar el template
    def get_context_data(self, **kwargs):
        pass

    # Función que se ejecuta en caso que el formulario sea valido
    def form_valid(self, form):
        pass


def iniciar_sesion(request):
    pass
