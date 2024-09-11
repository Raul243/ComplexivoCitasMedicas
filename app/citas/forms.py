from django import forms 
from .models import CitaMedica
from app.medical.models import *
from app.paciente.models import *
from app.colecciones.models import *


class CitaMedicaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    hora = forms.ChoiceField(
        choices=CitaMedica.HORA_OPCIONES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    motivo = forms.ChoiceField(
        choices=CitaMedica.MOTIVO_OPCIONES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    especialidad = forms.ModelChoiceField(
        queryset=Especialidad.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',  # Clase para aplicar estilos (por ejemplo, de Bootstrap)
        }),
        empty_label="Selecciona una especialidad"  # Etiqueta para el campo vacío
    )
        
    medico = forms.ModelChoiceField(
        queryset=Medico.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',  # Clase para aplicar estilos (por ejemplo, de Bootstrap)
        }),
        empty_label="Seleccione un medico"  # Etiqueta para el campo vacío
    )
    
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',  # Clase para aplicar estilos (por ejemplo, de Bootstrap)
        }),
        empty_label="Seleccione un medico"  # Etiqueta para el campo vacío
    )
    
    class Meta:
        model = CitaMedica
        fields = ['fecha', 'hora', 'especialidad', 'medico', 'paciente', 'motivo',]
        

class CitaMedicoForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['diagnostico', 'examenes']  # Campos solo editables por el médico

