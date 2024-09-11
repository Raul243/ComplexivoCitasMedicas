from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from app.colecciones.forms import *
from app.colecciones.models import *

# Vistas para listar examenes
class ExamenView(LoginRequiredMixin, ListView):
    model = Examen
    context_object_name = "obj"
    template_name = "colecciones/examen_list.html"
    login_url = 'inicio:login'
    
# Vista para crear examen
class ExamenNew(LoginRequiredMixin, CreateView):
    model = Examen
    template_name = "colecciones/examen_add.html"
    form_class = ExamenForm
    success_url = reverse_lazy("colecciones:examen_list")
    login_url = 'inicio:login'

    def form_valid(self, form):
        # No necesitamos asignar usuario_registro o usuario_modificacion
        return super().form_valid(form)
    
# Vista de clase para editar examen
class ExamenEdit(LoginRequiredMixin, UpdateView):
    template_name = "colecciones/examen_add.html"
    login_url = 'inicio:login'
    form_class = ExamenForm
    model = Examen
    context_object_name = "obj"
    success_url = reverse_lazy("colecciones:examen_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
# Vista de función para inactivar examen
def examen_inactivate(request, id):
    examen = Examen.objects.filter(pk=id).first()
    contexto = {}
    template_name = "colecciones/colecciones_delete.html "

    if not examen:
        return redirect("colecciones:examen_list")
    
    if request.method=='GET':
        contexto = {'obj':examen}

    if request.method=='POST':
        examen.estado = False
        examen.save()
        return redirect("colecciones:examen_list")

    return render(request, template_name, contexto)  



# Vista de clase para listar Diagnoticos
class DiagnosticoView(LoginRequiredMixin, ListView):
    model = Diagnostico
    context_object_name = "obj"
    template_name = "colecciones/diagnostico_list.html"
    login_url = 'inicio:login'
    

# Vista de clase para crear Diagnostico
class DiagnosticoNew(LoginRequiredMixin, CreateView):
    model = Diagnostico
    template_name = "colecciones/diagnostico_add.html"
    form_class = DiagnosticoForm
    success_url = reverse_lazy("colecciones:diagnostico_list")
    login_url = 'inicio:login'

    def form_valid(self, form):
        # No necesitamos asignar usuario_registro o usuario_modificacion
        return super().form_valid(form)
    
# Vista de clase para editar Diagnostico
class DiagnosticoEdit(LoginRequiredMixin, UpdateView):
    model = Diagnostico
    template_name = "colecciones/diagnostico_add.html"
    login_url = 'inicio:login'
    form_class = DiagnosticoForm
    success_url = reverse_lazy("colecciones:diagnostico_list")
    context_object_name = "obj"
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
# Vista de función para inactivar diagnostico
def diagnostico_inactivate(request, id):
    diagnostico = Diagnostico.objects.filter(pk=id).first()
    contexto = {}
    template_name = "colecciones/colecciones_delete.html "

    if not diagnostico:
        return redirect("colecciones:diagnostico_list")
    
    if request.method=='GET':
        contexto = {'obj':diagnostico}

    if request.method=='POST':
        diagnostico.estado = False
        diagnostico.save()
        return redirect("colecciones:diagnostico_list")

    return render(request, template_name, contexto)  


# Vistas para Colección Medicinas
class MedicinaView(LoginRequiredMixin, ListView):
    model = Medicina
    context_object_name = "obj"
    template_name = "colecciones/medicina_list.html"
    login_url = 'inicio:login'


class MedicinaNew(LoginRequiredMixin, CreateView):
    model = Medicina
    template_name = "colecciones/medicina_add.html"
    form_class = MedicinaForm
    success_url = reverse_lazy("colecciones:medicina_list")
    login_url = 'inicio:login'

    def form_valid(self, form):
        # No necesitamos asignar usuario_registro o usuario_modificacion
        return super().form_valid(form)
    
# Vista de clase para editar Especialidades
class MedicinaEdit(LoginRequiredMixin, UpdateView):
    model = Medicina
    template_name = "colecciones/medicina_add.html"
    login_url = 'inicio:login'
    form_class = MedicinaForm
    success_url = reverse_lazy("colecciones:medicina_list")
    context_object_name = "obj"
    
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
# Vista de función para inactivar especialidades
def medicina_inactivate(request, id):
    medicina = Medicina.objects.filter(pk=id).first()
    contexto = {}
    template_name = "colecciones/colecciones_delete.html "

    if not medicina:
        return redirect("colecciones:medicina_list")
    
    if request.method=='GET':
        contexto = {'obj':medicina}

    if request.method=='POST':
        medicina.estado = False
        medicina.save()
        return redirect("colecciones:medicina_list")

    return render(request, template_name, contexto)  
