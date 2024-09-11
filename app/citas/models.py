from django.db import models
from django.utils import timezone
from app.medical.models import *
from app.paciente.models import *
from app.colecciones.models import *
from datetime import date


class CitaMedica(models.Model):
    HORA_OPCIONES = [
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
        ('17:30', '17:30'),
    ]

    MOTIVO_OPCIONES = [
        ('Revision de Examenes', 'Revisión de Exámenes'),
        ('Cita Medica', 'Cita Médica'),
    ]

    fecha = models.DateField(default=timezone.now)
    hora = models.CharField(max_length=5, choices=HORA_OPCIONES)
    especialidad = models.CharField(max_length=100)  # Puedes ajustar si tienes un modelo de especialidades
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=50, choices=MOTIVO_OPCIONES)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.SET_NULL, null=True, blank=True)
    examenes = models.ManyToManyField(Examen, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    @property
    def edad(self):
        today = timezone.now().date()
        if self.paciente.fecha_nacimiento:
            return today.year - self.paciente.fecha_nacimiento.year - ((today.month, today.day) < (self.paciente.fecha_nacimiento.month, self.paciente.fecha_nacimiento.day))
        return None

    def save(self, *args, **kwargs):
        # Calcula y guarda la edad al crear la cita
        if self.paciente and self.paciente.fecha_nacimiento:
            self.edad_paciente = self.edad
        super().save(*args, **kwargs)
    
