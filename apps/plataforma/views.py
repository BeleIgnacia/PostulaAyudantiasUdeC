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
        # Esta linea se repite siempre, solo le cambian la class
        context = super(RegistrarAlumno, self).get_context_data(**kwargs)

        # Aquí añadimos lo que queramos al context, en este caso un formulario
        # El context lo recibe el template y lo maneja el navegador
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        # Al retornar se entrega el context al navegador
        return context

    # Función que se ejecuta en caso que el formulario sea valido
    def form_valid(self, form):
        pass


def iniciar_sesion(request):
    pass
