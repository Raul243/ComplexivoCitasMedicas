from django.urls import path
from django.contrib.auth import views as views_auth
from app.colecciones.views import *

urlpatterns = [
    
    # urls para examenes
    path('examen/',ExamenView.as_view(), name='examen_list'),
    path('examen/add',ExamenNew.as_view(), name='examen_new'),
    path('examen/new/<int:pk>',ExamenEdit.as_view(), name='examen_edit'),
    path('examen/inactivate/<int:id>',examen_inactivate, name='examen_inactivate'),
    
    # urls para diagnosticos
    path('diagnostico/',DiagnosticoView.as_view(), name='diagnostico_list'),
    path('diagnostico/add',DiagnosticoNew.as_view(), name='diagnostico_new'),
    path('diagnostico/new/<int:pk>',DiagnosticoEdit.as_view(), name='diagnostico_edit'),
    path('diagnostico/inactivate/<int:id>',diagnostico_inactivate, name='diagnostico_inactivate'),
    
    # urls para medicinas
    path('medicina/',MedicinaView.as_view(), name='medicina_list'),
    path('medicina/add',MedicinaNew.as_view(), name='medicina_new'),
    path('medicina/new/<int:pk>',MedicinaEdit.as_view(), name='medicina_edit'),
    path('medicina/inactivate/<int:id>',medicina_inactivate, name='medicina_inactivate'),
]
