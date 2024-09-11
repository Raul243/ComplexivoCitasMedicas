from django import forms
from .models import *

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['codigo', 'nombre', 'estado']

    def __init__(self, *args, **kwargs):
        super(ExamenForm, self).__init__(*args, **kwargs)
       
       
class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['codigo', 'nombre', 'estado']

    def __init__(self, *args, **kwargs):
        super(DiagnosticoForm, self).__init__(*args, **kwargs)
       

class MedicinaForm(forms.ModelForm):
    class Meta:
        model = Medicina
        fields = ['codigo', 'nombre', 'estado']

    def __init__(self, *args, **kwargs):
        super(MedicinaForm, self).__init__(*args, **kwargs)
       