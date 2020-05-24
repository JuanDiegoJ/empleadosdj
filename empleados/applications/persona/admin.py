from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )

    def full_name(self, obj):
        #Toda la operación que se necesite
        print(obj)
        #Trae cada registro que se está iterando en el administrador de Django
        return f'{obj.first_name} {obj.last_name}'

    search_fields = (
        'first_name',
    )

    list_filter = ('job', 'departamento')

    filter_horizontal = ('habilidades',)
    
admin.site.register(Empleado, EmpleadoAdmin)