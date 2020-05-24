from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Empleado
# Create your views here.
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """Página de inicio"""
    template_name = 'inicio.html'

#1. Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 3

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            #Indica que dentro del parametro esté el contenido de la palabra clave
            Q(departamento__name__icontains=palabra_clave) |
            Q(first_name__icontains=palabra_clave) |
            Q(last_name__icontains=palabra_clave)
        )
        return lista


#2. Listar todos los empleados que pertenecen a un área de la empresa
class ListByArea(ListView):
    template_name = 'persona/list_area.html'
    model = Empleado
    context_object_name = 'empleados'

    def get_queryset(self):
        #Se declara una nueva variable
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
            departamento__name__icontains=area
        )

        return lista


#3. Listar empleados por trabajo

class ListByJob(ListView):
    template_name = 'persona/list_job.html'
    model = Empleado

    def get_queryset(self):
        #Se declara una nueva variable
        job_f = self.kwargs['job']
        lista = Empleado.objects.filter(
            job = job_f
        )

        return lista
        

#4. Listar los empleados por palabra clave

class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", )
        lista = Empleado.objects.filter(
            #Indica que dentro del parametro esté el contenido de la palabra clave
            first_name__icontains=palabra_clave
        )
        return lista

#5. Listar habilidades por empleado

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):

        empleado_first_name = self.request.GET.get("search_fn", )
        empleado = Empleado.objects.get(first_name=empleado_first_name) 
        return empleado.habilidades.all()

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    model = Empleado
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    slug_field = 'first_name'

class SuccessView(TemplateView):
    template_name = 'persona/success.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    """ fields = ['first_name', 'last_name', 'job'] """
    form_class = EmpleadoForm

    success_url = reverse_lazy('persona_app:correcto')
    
    def  form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpeladoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request, *args, **kwargs)

    """ def  form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form) """

class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')
