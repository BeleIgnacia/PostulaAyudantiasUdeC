from django import forms
from apps.plataforma.models import Ayudantia,Postulacion


class RegistrarPostulacionAyudantia(forms.ModelForm):
    class Meta:
        model = Ayudantia
        fields = [
            'cursoid',
            'semestre',
            'descripcion',
            'horario',
            'requisitos',
            'puestos',
        ]
        labels = {
            'cursoid': 'Código del curso',
            'semestre': 'Semestre',
            'descripcion': 'Descripción breve',
            'horario': 'Horario',
            'requisitos': 'Requisitos del curso',
            'puestos':'Nº de puestos vacantes',
        }
        widgets = {
            'cursoid': forms.TextInput(attrs={'placeholder': 'Código'}),
            'semestre': forms.TextInput(attrs={'placeholder': 'Semestre'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Descripción'}),
            'horario': forms.TextInput(attrs={'placeholder': 'Horario'}),
            'requisitos': forms.TextInput(attrs={'placeholder': 'Requisitos'}),
            'puestos': forms.TextInput(attrs={'placeholder': 'Nº de puestos vacantes'}),
        }

