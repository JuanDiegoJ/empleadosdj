from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

class DepartamentoListView(ListView):
    template_name = 'departamento/list_departamento.html'
    model = Departamento

class DepartamentoDetailView(DetailView):
    template_name = "departamento/detail_departamento.html"
    model = Departamento
    slug_field = 'name'
    context_object_name = 'departamento'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        #Crea una instancia del modelo departamento
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shorname']
        )
        #Guarda los datos creados
        depa.save()

        #Se asignan los valores
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        #Se crea una instancia del modelo Empleado y se usa el atributo create
        #Al usar el atributo create no es necesario usar posteriormente el save()
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)