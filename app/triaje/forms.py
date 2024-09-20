from django import forms
from .models import Triaje
from app.paciente.models import Paciente

class TriajeForm(forms.ModelForm):
    PRIORIDAD_OPCIONES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta')
    ]

    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        empty_label="Selecciona un paciente"
    )
    frecuencia_cardiaca = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Frecuencia cardíaca (60-100)',
        })
    )
    frecuencia_respiratoria = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Frecuencia respiratoria (12-20)',
        })
    )
    presion_arterial_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Presión arterial mínima (80-84 mmHg)',
        })
    )
    presion_arterial_max = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Presión arterial máxima (120-129 mmHg)',
        })
    )
    temperatura_corporal = forms.DecimalField(
        max_digits=4, decimal_places=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Temperatura corporal (12.0-40.0)',
        })
    )
    spo2 = forms.DecimalField(
        max_digits=4, decimal_places=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nivel de saturación de oxígeno (70.0-100.0)',
        })
    )
    prioridad = forms.ChoiceField(
        choices=PRIORIDAD_OPCIONES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    estado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    class Meta:
        model = Triaje
        fields = [
            'paciente', 'frecuencia_cardiaca', 'frecuencia_respiratoria',
            'presion_arterial_min', 'presion_arterial_max', 'temperatura_corporal',
            'spo2', 'prioridad', 'estado'
        ]

    def clean(self):
        cleaned_data = super().clean()
        # Puedes agregar validaciones personalizadas aquí si es necesario
        return cleaned_data
