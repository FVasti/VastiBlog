from django import forms
from .models import Autor, Articulo, Comentario

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

class BusquedaArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False)
