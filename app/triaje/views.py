from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from app.triaje.models import *
from app.triaje.forms import *


# Create your views here.# Vistas para medicos
class TriajeView(LoginRequiredMixin, ListView):
    template_name = "triaje/triaje_list.html"
    login_url = 'inicio:login'
    model = Triaje
    context_object_name = "obj"
    
# vista para crear medicos
class TriajeNew(LoginRequiredMixin, CreateView):
    model = Triaje
    template_name = "triaje/triaje_add.html"
    form_class = TriajeForm
    success_url = reverse_lazy("triajes:triaje_list")
    login_url = 'inicio:login'
    
    def form_valid(self, form):
        # Aquí, el usuario ya se creará desde el formulario, no es necesario hacer más modificaciones
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Imprime los errores del formulario en la consola
        return self.render_to_response(self.get_context_data(form=form))
    
    
# Vista de clase para editar medicos
class TriajeEdit(LoginRequiredMixin, UpdateView):
    template_name = "triaje/triaje_add.html"
    login_url = 'bases:login'
    form_class = TriajeForm
    model = Triaje
    context_object_name = "obj"
    success_url = reverse_lazy("triajes:triaje_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
    
# Vista de función para inactivar medicos
def triaje_inactivate(request, id):
    triaje = Triaje.objects.filter(pk=id).first()
    contexto = {}
    template_name = "triaje/triaje_delete.html"

    if not triaje:
        return redirect("triajes:triaje_list")
    
    if request.method == 'GET':
        contexto = {'obj': triaje, 'tipo_objeto': 'triaje'}

    if request.method == 'POST':
        triaje.estado = False
        triaje.save()
        return redirect("triajes:triaje_list")

    return render(request, template_name, contexto)

