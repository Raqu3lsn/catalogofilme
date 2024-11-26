from django import forms
from .models import Catalogo, Filme


class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = '__all__'

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'