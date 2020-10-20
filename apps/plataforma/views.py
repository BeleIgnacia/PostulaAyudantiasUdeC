from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from apps.plataforma.forms import RegistrarUsuarioForm, NuevoCursoForm
from apps.plataforma.models import Usuario, Curso


# Esta es una vista para creación de un modelo
# por eso hereda de CreateView
class RegistrarAlumno(CreateView):
    # Se define el modelo sobre el que añade una instancia
    model = Usuario
    # El formulario que se despliega dentro de la vista
    form_class = RegistrarUsuarioForm
    # El html que se muestra en el navegador
    template_name = 'plataforma/registrar_alumno.html'
    # La dirección en caso de que el formulario sea correcto
    # aquí se utiliza namespace:name
    success_url = reverse_lazy('iniciar_sesion')

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
        # Recibe formulario como una instancia
        instance = form.save(commit=False)
        # Aquí pueden editar la instancia
        # En este caso usaremos el email como username igualmente
        instance.username = instance.email
        # Se guarda la instancia en la BD
        instance.save()
        # Redirect
        return HttpResponseRedirect(reverse_lazy('iniciar_sesion'))


# La vista de inciar sesión esta definida como función
# pueden utilizarla como quieran
# pero usarla como función es un poco feo -_-
def iniciar_sesion(request):
    # Metodos post en caso de hacer un POST obviously
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect()
            # Instancia de objeto usuario
            usuario = Usuario.objects.get(username=username)
            # Almacena la pk de usuario para utilizar a futuro
            request.session['pk_usuario'] = usuario.pk
            request.session['es_docente'] = usuario.es_docente
            request.session['es_administrador'] = usuario.es_administrador
            request.session['first_name'] = usuario.first_name
            request.session['last_name'] = usuario.last_name
            # Redirige
            return HttpResponseRedirect(reverse('plataforma:dashboard'))
        pass

    # Contexto con variables que se le entrega al template
    context = {}
    # Despliega el template dentro del navegador
    return render(request, 'plataforma/login.html', context)


# Pantalla principal luego de inciar sesión
class Dashboard(TemplateView):
    template_name = 'plataforma/dashboard.html'


class RegistrarDocente(CreateView):
    model = Usuario
    form_class = RegistrarUsuarioForm
    template_name = 'plataforma/registrar_docente.html'
    success_url = reverse_lazy('plataforma:registrar_docente')

    def get_context_data(self, **kwargs):
        context = super(RegistrarDocente, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.username = instance.email
        instance.es_docente = True
        instance.save()
        return HttpResponseRedirect(reverse_lazy('plataforma:registrar_docente'))


class NuevoCurso(CreateView):
    model = Curso
    form_class = NuevoCursoForm
    template_name = 'plataforma/nuevo_curso.html'
    success_url = reverse_lazy('plataforma:nuevo_curso')

    def form_valid(self, form):
        instance = form.save(commit=False)
        docente = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        instance.docente = docente
        instance.save()
        return HttpResponseRedirect(reverse_lazy('plataforma:nuevo_curso'))

