from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from django.utils import timezone 

from app.paciente.forms import *
from app.paciente.models import *

# Vistas para listar pacientes
class PacienteView(LoginRequiredMixin, ListView):
    model = Paciente
    context_object_name = "obj"
    template_name = "paciente/paciente_list.html"
    login_url = 'inicio:login'
    

# Vista para crear paciente
class PacienteNew(LoginRequiredMixin, CreateView):
    model = Paciente
    template_name = "paciente/paciente_add.html"
    form_class = PacienteForm
    success_url = reverse_lazy("paciente:paciente_list")
    login_url = 'inicio:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

    def form_valid(self, form):
        # Aquí, el usuario ya se creará desde el formulario
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Imprime los errores del formulario en la consola
        return self.render_to_response(self.get_context_data(form=form))

    
# Vista de clase para editar paciente
class PacienteEdit(LoginRequiredMixin, UpdateView):
    model = Paciente
    template_name = "paciente/paciente_add.html"
    form_class = PacienteForm
    context_object_name = "obj"
    success_url = reverse_lazy("paciente:paciente_list")
    login_url = 'inicio:login'
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context
    
    
# Vista de función para inactivar paciente
def paciente_inactivate(request, id):
    paciente = Paciente.objects.filter(pk=id).first()
    contexto = {}
    template_name = "paciente/paciente_delete.html "

    if not paciente:
        return redirect("paciente:paciente_list")
    
    if request.method=='GET':
        contexto = {'obj':paciente}

    if request.method=='POST':
        paciente.estado = False
        paciente.save()
        return redirect("paciente:paciente_list")

    return render(request, template_name, contexto)  
