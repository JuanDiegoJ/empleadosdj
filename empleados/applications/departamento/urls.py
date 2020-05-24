from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path(
        'new-departamento/', 
        views.NewDepartamentoView.as_view(), 
        name='nuevo_departamento'
    ),
    path(
        'lista_departamentos/', 
        views.DepartamentoListView.as_view(), 
        name='list_departamento'
    ),
    path(
        'detalle_departamentos/<slug>', 
        views.DepartamentoDetailView.as_view(), 
        name='det_departamento'
    ),
]
