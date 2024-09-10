from django import forms
from django.contrib.auth.models import User 
from .models import *
from django.core.exceptions import ValidationError
from django.utils import timezone

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion', 'estado']

    def __init__(self, *args, **kwargs):
        super(EspecialidadForm, self).__init__(*args, **kwargs)
        # Aquí puedes personalizar los widgets o agregar validaciones si es necesario
        
        
class MedicoForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
    )
    fecha_nacimiento = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Selecciona una fecha'
        })
    )
    especialidad = forms.ModelChoiceField(
        queryset=Especialidad.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        empty_label="Selecciona una especialidad"
    )

    class Meta:
        model = Medico
        fields = ['identificacion', 'apellidos', 'nombres', 'telefono', 'direccion', 'ciudad_residencia', 'fecha_nacimiento', 'genero', 'estado', 'especialidad']

    def save(self, commit=True):
        # Primero creamos el usuario asociado
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        # Luego, creamos el médico y lo asociamos con el usuario
        medico = super(MedicoForm, self).save(commit=False)
        medico.user = user  # Asocia el usuario creado
        if commit:
            medico.save()
        return medico
