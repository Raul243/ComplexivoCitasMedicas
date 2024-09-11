from django.urls import path
from django.contrib.auth import views as views_auth
from app.citas.views import *

urlpatterns = [
    
    # urls para citas
    path('list/',CitaMedicaView.as_view(), name='citas_list'),
    path('add/',CitaMedicaNew.as_view(), name='citas_new'),
]