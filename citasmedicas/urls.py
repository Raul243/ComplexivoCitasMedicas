"""
URL configuration for citasmedicas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('citasmedicas/', include(('app.citas.urls', 'citas'), namespace = 'citas')),
    path('paciente/', include(('app.paciente.urls', 'paciente'), namespace = 'paciente')),
    path('colecciones/',include(('app.colecciones.urls','colecciones'), namespace = 'colecciones')),
    path('medical/',include(('app.medical.urls','medical'), namespace = 'medical')),
    path('',include(('app.inicio.urls','inicio'), namespace = 'inicio')),
    path('admin/', admin.site.urls),
]
