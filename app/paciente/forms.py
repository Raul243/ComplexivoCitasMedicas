from django import forms
from django.contrib.auth.models import User 
from .models import Paciente
from django.core.exceptions import ValidationError
from django.utils import timezone

class PacienteForm(forms.ModelForm):
    # Campos adicionales para crear el usuario asociado
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Formato año-mes-día
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',  # Clase para aplicar estilos (por ejemplo, de Bootstrap)
            'placeholder': 'Selecciona una fecha'  # Placeholder opcional
        })
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase de Bootstrap
            'placeholder': 'Nombre de usuario'  # Placeholder opcional
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',  # Clase de Bootstrap
            'placeholder': 'Contraseña'  # Placeholder opcional
        })
    )

    class Meta:
        model = Paciente
        fields = ['identificacion', 'apellidos', 'nombres', 'telefono', 'direccion', 'ciudad_residencia', 'fecha_nacimiento', 'genero']

    def save(self, commit=True):
        # Primero creamos el usuario asociado
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        # Luego, creamos el paciente y lo asociamos con el usuario
        paciente = super(PacienteForm, self).save(commit=False)
        paciente.user = user  # Asocia el usuario creado
        if commit:
            paciente.save()
        return paciente

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if fecha_nacimiento > timezone.now().date():
            raise ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        return fecha_nacimiento
