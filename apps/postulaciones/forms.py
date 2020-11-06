from django import forms
from apps.postulaciones.models import Ayudantia,Postulacion
from apps.plataforma.models import Usuario, Curso

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


class ResgistrarPostulacionAlumno(forms.Modelform):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido1',
            'apellido2',
            'matricula',
            'carrera',
            'semestrecarrera',
            'semestreramo',
            'nota',          
        ]
        labels = {
            'nombre':'Nombre',
            'apellido1':'Apellido Paterno',
            'apellido2':'Apellido Materno',
            'matricula':'Matrícula',
            'carrera':'Carrera',
            'semestrecarrera':'Semestre actual',
            'semestreramo':'Semestre de rendición',
            'nota':'Nota',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'placeholder': 'Su nombre', 'class': 'form-control'}),
            'apellido1':forms.TextInput(attrs={'placeholder': 'Apellido Paterno', 'class': 'form-control'}),
            'apellido2':forms.TextInput(attrs={'placeholder': 'Apellido Materno', 'class': 'form-control'}),
            'matricula':forms.TextInput(attrs={'placeholder': 'Ingrese su matrícula', 'class': 'form-control'}),
            'carrera':forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'semestrecarrera':forms.TextInput(attrs={'placeholder': 'Ej: 2020-1', 'class': 'form-control'}),
            'semestreramo':forms.TextInput(attrs={'placeholder': 'Ej: 2019-2', 'class': 'form-control'}),
            'nota':forms.TextInput(attrs={'placeholder': 'Promedio con el que aprobó', 'class': 'form-control'}),
        }