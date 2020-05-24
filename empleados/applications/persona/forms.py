from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
            'image'
        )

        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
