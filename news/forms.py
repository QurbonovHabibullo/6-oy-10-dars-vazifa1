from django import forms
from .models import Turlar,Gullar

class TurForm(forms.Form):
    name = forms.CharField(max_length=100,label ="Tur nomi")
    description = forms.CharField(widget=forms.Textarea,label="Ta'rifi",required=False)
    
    
class GulForm(forms.Form):
    name = forms.CharField(max_length=100,label="Gul nomi")
    description = forms.CharField(widget=forms.Textarea,label="Gul ta'rifi",required=False)
    price = forms.DecimalField(max_digits=10,decimal_places=2,label="narxi")
    turi = forms.ModelChoiceField(queryset=Turlar.objects.all(),label="Tur nomi")
    