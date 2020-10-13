from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.plataforma.models import Usuario


# Formulario para registro de alumno
# El formulario hereda del formulario de creación de usuario por defecto
class RegistrarAlumnoForm(UserCreationForm):
    # Se define una subclase Meta en la que se determinan los parametros de entrada
    class Meta:
        # Model es el modelo en la bd que utiliza para saber donde añadir la entrada
        model = Usuario
        # Fields son los campos que utilizaremos
        # Podemos añadir y quitar campos siempre que permitan ser nulos o tengan default
        fields = [
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
        # Labels son nombres que utilizaremos para guiarnos dentro del template
        labels = {
            'email': 'Dirección de correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'password1': 'Contraseña',
            'password2': 'Repetir contraseña'
        }
        # widgets definen la entrada que se representa en el form
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Dirección de correo'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        }
