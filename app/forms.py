from django import forms
from . import models
class CoffeForms(forms.ModelForm):
    class Meta:
        model=models.CoffeReporte
        fields=["titulo","csv"]
