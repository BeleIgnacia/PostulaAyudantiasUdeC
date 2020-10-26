from django import forms
from apps.postulaciones.models import Ayudantia,Postulacion


class RegistrarPostulacionAyudantia(forms.ModelForm):
    class Meta:
        model = Ayudantia
        fields = [
            'curso',
            'semestre',
            'descripcion',
            'horario',
            'requisito',
            'puestos',
        ]
        labels = {
            'curso': 'Curso',
            'semestre': 'Semestre',
            'descripcion': 'Descripción breve',
            'horario': 'Horario',
            'requisito': 'Requisitos del curso',
            'puestos':'Nº de puestos vacantes',
        }
        widgets = {
            'semestre': forms.NumberInput(attrs={'placeholder': 'Semestre', 'class': 'form-control', 'max': 3, 'min': 1}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción', 'class': 'form-control'}),
            'horario': forms.TextInput(attrs={'placeholder': 'Ej: Martes 10:15 - 12:00', 'class': 'form-control'}),
            'requisito': forms.TextInput(attrs={'placeholder': 'Ej: Ingeniería de Software 2', 'class': 'form-control'}),
            'puestos': forms.NumberInput(attrs={'placeholder': 'Nº de puestos vacantes', 'class': 'form-control', 'max': 10, 'min': 1}),
        }

