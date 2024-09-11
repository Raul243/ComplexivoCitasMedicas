from django.urls import path
from django.contrib.auth import views as views_auth
from app.medical.views import *

urlpatterns = [
    
    #urls para especialidades
    path('especialidad/',EspecialidadView.as_view(), name='especialidad_list'),
    path('especialidad/add',EspecialidadNew.as_view(), name='especialidad_new'),
    path('especialidad/new/<int:pk>',EspecialidadEdit.as_view(), name='especialidad_edit'),
    path('especialidad/inactivate/<int:id>',especialidad_inactivate, name='especialidad_inactivate'),
    
    #urls medicos
    path('medico/',MedicoView.as_view(), name='medico_list'),
    path('medico/add',MedicoNew.as_view(), name='medico_new'),
    path('medico/new/<int:pk>',MedicoEdit.as_view(), name='medico_edit'),
    path('medico/inactivate/<int:id>',medico_inactivate, name='medico_inactivate'),
]
