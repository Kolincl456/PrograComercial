from django import forms
from django import forms
from .models import Publicaion

class PublicacionForms(forms.ModelForm):

    class Meta:
        model = Publicaion
        fields = ('titulo', 'texto', )