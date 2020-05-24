from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'listar-todos-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='list_empleados'
    ),
    path(
        'listar-by-area/<name>', 
        views.ListByArea.as_view(),
        name='list_by_area'
    ),
    path(
        'listar-by-job/<job>', 
        views.ListByJob.as_view()
    ),
    path(
        'buscar-empleado/', 
        views.ListEmpleadosByKword.as_view()
    ),
    path(
        'listar-habilidades-empleado/', 
        views.ListHabilidadesEmpleado.as_view()
    ),
    path(
        'ver-empleado/<slug>/', 
        views.EmpleadoDetailView.as_view(),
        name='det_empleado'
    ),
    path(
        'registrar-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='add_empleado'
    ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'actualizar-empleado/<pk>/', 
        views.EmpeladoUpdateView.as_view(), 
        name='actualizar'
    ),
    path(
        'eliminar-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar'
    ),
    path(
        'lista-empleados-admin/', 
        views.ListaEmpleadosAdmin.as_view(), 
        name='empleados_admin'
    ),
]