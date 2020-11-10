from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib import messages

from apps.plataforma.forms import RegistrarUsuarioForm, NuevoCursoForm, ActualizarPerfilForm
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

        emails = Usuario.objects.values_list('email', flat=True)
        for email in emails:
            if instance.email == email:
                messages.error(self.request, "Ya existe un usuario con esta dirección de correo.")
                return HttpResponseRedirect(self.request.path_info)

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
            request.session['email'] = usuario.email
            # Redirige
            return HttpResponseRedirect(reverse('plataforma:dashboard'))
        pass

    # Contexto con variables que se le entrega al template
    context = {}
    # Despliega el template dentro del navegador
    return render(request, 'plataforma/login.html', context)


def cerrar_sesion(request):
    # Finalizamos la sesión
    logout(request)
    # Redireccionamos a la portada
    return HttpResponseRedirect(reverse('navegacion:inicio'))


# Pantalla principal luego de inciar sesión
class Dashboard(LoginRequiredMixin, TemplateView):
    login_url = '/iniciar/'
    template_name = 'plataforma/dashboard.html'


class RegistrarDocente(UserPassesTestMixin, CreateView):
    login_url = '/iniciar/'
    model = Usuario
    form_class = RegistrarUsuarioForm
    template_name = 'plataforma/registrar_docente.html'
    success_url = reverse_lazy('plataforma:registrar_docente')

    def test_func(self):
        return self.request.session.get('es_administrador')

    def get_context_data(self, **kwargs):
        context = super(RegistrarDocente, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.username = instance.email
        instance.es_docente = True

        emails = Usuario.objects.values_list('email', flat=True)
        for email in emails:
            if instance.email == email:
                messages.error(self.request, "Ya existe un usuario con esta dirección de correo.")
                return HttpResponseRedirect(self.request.path_info)

        instance.save()
        return HttpResponseRedirect(reverse_lazy('plataforma:registrar_docente'))


class NuevoCurso(UserPassesTestMixin, CreateView):
    login_url = '/iniciar/'
    model = Curso
    form_class = NuevoCursoForm
    template_name = 'plataforma/nuevo_curso.html'
    success_url = reverse_lazy('plataforma:nuevo_curso')

    def test_func(self):
        return self.request.session.get('es_docente')

    def form_valid(self, form):
        instance = form.save(commit=False)

        codigos = Curso.objects.values_list('codigo', flat=True)
        for codigo in codigos:
            if instance.codigo == codigo:
                messages.error(self.request, "Ya existe este curso.")
                return HttpResponseRedirect(self.request.path_info)

        docente = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        instance.docente = docente
        instance.save()
        return HttpResponseRedirect(reverse_lazy('plataforma:nuevo_curso'))


# Editar perfil
class ActualizarPerfil(LoginRequiredMixin, UpdateView):
    login_url = '/iniciar/'
    model = Usuario
    form_class = ActualizarPerfilForm
    template_name = 'plataforma/editar_perfil.html'

    def get_context_data(self, **kwargs):
        context = super(ActualizarPerfil, self).get_context_data()
        # Determina si el perfil ingresado por pk es mio
        context['mi_perfil'] = False
        path = self.request.path_info.split("/")
        if self.request.session.get('pk_usuario', '') == int(path[-2]):
            context['mi_perfil'] = True
        return context

    def get_success_url(self):
        return reverse('plataforma:perfil', kwargs={'pk': self.object.pk})
