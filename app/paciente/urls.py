from django.urls import path
from django.contrib.auth import views as views_auth
from app.paciente.views import *

urlpatterns = [
    
    # urls para pacientes
    path('list/',PacienteView.as_view(), name='paciente_list'),
    path('add/',PacienteNew.as_view(), name='paciente_new'),
    path('edit/<int:pk>',PacienteEdit.as_view(), name='paciente_edit'),
    path('inactivate/<int:id>',paciente_inactivate, name='paciente_inactivate'),
]