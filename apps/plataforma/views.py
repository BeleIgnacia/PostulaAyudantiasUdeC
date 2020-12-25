import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, ListView

from apps.plataforma.forms import RegistrarUsuarioForm, ActualizarPerfilForm
from apps.plataforma.models import Usuario, Curso


# Esta es una vista para creación de un modelo
# por eso hereda de CreateView

# ambos metodos retornan una lista con los dict de datos
def get_cursos_list(semestre, email):
    url = "http://proyectoinformatico.udec.cl/proyecto/1/2020{}00/{}".format(str(semestre), str.upper(email))
    json_data = requests.get(url).json()
    return json_data


def get_alumno_verify(email):
    url = "http://proyectoinformatico.udec.cl/proyecto/2/{}".format(str.upper(email))
    json_data = requests.get(url).json()
    return json_data


semestre_actual = 2


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = RegistrarUsuarioForm
    template_name = 'plataforma/registrar_alumno.html'
    success_url = reverse_lazy('iniciar_sesion')

    def get_context_data(self, **kwargs):
        context = super(RegistrarUsuario, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.email = str.lower(usuario.email)
            usuario.username = usuario.email

            # En primer lugar se verifica el correo
            if Usuario.objects.filter(username=usuario.username).count() > 0:
                return HttpResponse("ya existe el usuario")

            # En segundo lugar se verifica si es docente o alumno
            cursos_list = get_cursos_list(semestre_actual, usuario.email)
            if len(cursos_list) > 0:  # Condición de docente para el semestre actual
                usuario.es_docente = True  # Se marca como docente
                usuario.save()  # Almacenamos el docente antes de crear cursos
                for curso in cursos_list:
                    Curso(
                        docente=usuario,
                        codigo=curso['codigoAsignatura'],
                        nombre=curso['nombreAsignatura'],
                        seccion=curso['seccion']
                    ).save()
                return HttpResponseRedirect(reverse_lazy('iniciar_sesion'))
            else:
                alumno_verify = get_alumno_verify(usuario.email)
                if len(alumno_verify) == 1:  # Condición de alumno
                    usuario.matricula = alumno_verify[0]['matricula']  # Asocia la matricula al alumno
                    usuario.save()
                    return HttpResponseRedirect(reverse_lazy('iniciar_sesion'))
            return HttpResponse("no es nada")


def iniciar_sesion(request):
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


class MisCursos(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'plataforma/desplegar_mis_cursos.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MisCursos, self).get_context_data()
        docente = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        context['cursos'] = Curso.objects.filter(docente=docente)
        return context

    def post(self, request, *args, **kwargs):
        id_curso = request.POST.get('id_curso')
        descripcion = request.POST.get('descripcion')
        docente = Usuario.objects.get(pk=self.request.session.get('pk_usuario', ''))
        if Curso.objects.filter(pk=id_curso, docente=docente).count() > 0:
            curso = Curso.objects.get(pk=id_curso)
            curso.descripcion = descripcion
            curso.save()
            return HttpResponseRedirect(reverse_lazy('plataforma:mis_cursos'))
        else:
            return HttpResponse("Usted no se encuentra autorizado a editar este curso")
