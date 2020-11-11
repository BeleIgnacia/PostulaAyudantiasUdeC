from django.db import models
from apps.plataforma.models import Usuario, Curso


class Ayudantia(models.Model):
    # Si se quita docente se desliga la ayudantia del docente y solo se asocia al curso
    # docente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    # Atributos
    semestre = models.IntegerField(default=2)
    horario = models.CharField(max_length=50)
    descripcion = models.TextField()
    requisito = models.CharField(max_length=50)
    puestos = models.IntegerField(default=1)

    def __str__(self):
        return 'Ayudantía de {}'.format(self.curso)


class Postulacion(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ayudantia = models.ForeignKey(Ayudantia, on_delete=models.CASCADE)
    # Atributos
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    estado = models.BooleanField(default=False)
    semestreramo=models.CharField(max_length=6)
    nota=models.IntegerField(default=0)

    def __str__(self):
        return 'Postulación de {} a {}'.format(self.alumno, self.ayudantia)
