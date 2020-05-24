from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):
    """Form definition for PruebaNAME."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        #En el atributo fields se muestran los campos que se quieren ver en el HTML
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese el texto aquí',
                    'class': 'titulo_prueba'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')
        return cantidad