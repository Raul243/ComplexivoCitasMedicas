from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.utils import timezone
from app.citas.forms import *
from app.citas.models import *
from django.urls import reverse_lazy

# Vistas para listar citas
class CitaMedicaView(LoginRequiredMixin, ListView):
    model = CitaMedica
    context_object_name = "obj"
    template_name = "citas/citas_list.html"
    login_url = 'inicio:login'


# vistas para crear cita medica
class CitaMedicaNew(LoginRequiredMixin, CreateView):
    model = CitaMedica
    template_name = 'citas/citas_add.html'
    form_class = CitaMedicaForm
    success_url = reverse_lazy("citas:citas_list")
    login_url = 'inicio:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

    def form_valid(self, form):
        paciente = form.cleaned_data['paciente']
        form.instance.edad_paciente = timezone.now().year - paciente.fecha_nacimiento.year
        return super().form_valid(form)

# vista para editar cita medica
class CitaMedicaEdit(LoginRequiredMixin, UpdateView):
    model = CitaMedica
    form_class = CitaMedicoForm
    template_name = 'citas/citas_add.html'
    success_url = reverse_lazy("citas:citas_list")
    login_url = 'inicio:login'
    
    def get_queryset(self):
        # Solo permitir que el médico edite citas a las que está asignado
        return CitaMedica.objects.filter(medico=self.request.user.medico)