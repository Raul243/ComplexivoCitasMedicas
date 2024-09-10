from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from app.medical.forms import *
from app.medical.models import *


# Vistas para Especialidades
class EspecialidadView(LoginRequiredMixin, ListView):
    template_name = "medical/especialidad_list.html"
    login_url = 'inicio:login'
    model = Especialidad
    context_object_name = "obj"

class EspecialidadNew(LoginRequiredMixin, CreateView):
    model = Especialidad
    template_name = "medical/especialidad_add.html"
    form_class = EspecialidadForm
    success_url = reverse_lazy("medical:especialidad_list")
    login_url = 'inicio:login'

    def form_valid(self, form):
        # No necesitamos asignar usuario_registro o usuario_modificacion
        return super().form_valid(form)
    
# Vista de clase para editar Especialidades
class EspecialidadEdit(LoginRequiredMixin, UpdateView):
    template_name = "medical/especialidad_add.html"
    login_url = 'bases:login'
    form_class = EspecialidadForm
    model = Especialidad
    context_object_name = "obj"
    success_url = reverse_lazy("medical:especialidad_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
# Vista de función para inactivar especialidades
def especialidad_inactivate(request, id):
    especialidad = Especialidad.objects.filter(pk=id).first()
    contexto = {}
    template_name = "medical/medical_delete.html"

    if not especialidad:
        return redirect("medical:especialidad_list")
    
    if request.method == 'GET':
        contexto = {'obj': especialidad, 'tipo_objeto': 'especialidad'}

    if request.method == 'POST':
        especialidad.estado = False
        especialidad.save()
        return redirect("medical:especialidad_list")

    return render(request, template_name, contexto)


# Vistas para medicos
class MedicoView(LoginRequiredMixin, ListView):
    template_name = "medical/medico_list.html"
    login_url = 'inicio:login'
    model = Medico
    context_object_name = "obj"
    
    
# vista para crear medicos
class MedicoNew(LoginRequiredMixin, CreateView):
    model = Medico
    template_name = "medical/medico_add.html"
    form_class = MedicoForm
    success_url = reverse_lazy("medical:medico_list")
    login_url = 'inicio:login'
    
    def form_valid(self, form):
        # Aquí, el usuario ya se creará desde el formulario, no es necesario hacer más modificaciones
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Imprime los errores del formulario en la consola
        return self.render_to_response(self.get_context_data(form=form))

    
# Vista de clase para editar medicos
class MedicoEdit(LoginRequiredMixin, UpdateView):
    template_name = "medical/medico_add.html"
    login_url = 'bases:login'
    form_class = MedicoForm
    model = Medico
    context_object_name = "obj"
    success_url = reverse_lazy("medical:medico_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
    
# Vista de función para inactivar medicos
def medico_inactivate(request, id):
    medico = Medico.objects.filter(pk=id).first()
    contexto = {}
    template_name = "medical/medical_delete.html"

    if not medico:
        return redirect("medical:medico_list")
    
    if request.method == 'GET':
        contexto = {'obj': medico, 'tipo_objeto': 'medico'}

    if request.method == 'POST':
        medico.estado = False
        medico.save()
        return redirect("medical:medico_list")

    return render(request, template_name, contexto)
