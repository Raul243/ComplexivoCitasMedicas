from django.urls import path
from app.triaje.views import *


urlpatterns = [
    # urls para triaje
    path('list/',TriajeView.as_view(), name='triaje_list'),
    path('add/',TriajeNew.as_view(), name='triaje_new'),
    path('edit/<int:pk>',TriajeEdit.as_view(), name='triaje_edit'),
    path('inactivate/<int:id>',triaje_inactivate, name='triaje_inactivate'),
]