from django import forms
from .models import Expediente


class ExpedienteForm(forms.ModelForm):

    class Meta:
        model = Expediente
        fields = ['codigo', 'tipo', 'descripcion', 'numero_folio', 'user']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Codigo'}),
            'tipo': forms.Select(attrs={'class': 'custom-select mr-sm-2 form-control-lg'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'numero_folio': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'user': forms.Select(attrs={'class': 'custom-select mr-sm-2 form-control-lg', 'placeholder': 'Usuario'}),

            
        }
        labels = {
            'codigo': '', 'tipo': '', 'descripcion': '','numero_folio': '', 'user': ''
        }


class ExpedienteUpdateForm(forms.ModelForm):

    class Meta:
        model = Expediente
        fields = ['codigo', 'tipo', 'descripcion', 'numero_folio', 'estado', 'flag']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Codigo'}),
            'tipo': forms.Select(attrs={'class': 'custom-select mr-sm-2 form-control-lg'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'numero_folio': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-control form-control-lg custom-checkbox'}),
            'flag': forms.CheckboxInput(attrs={'class': 'form-control form-control-lg custom-checkbox'})          
        }
        labels = {
            'codigo': '', 'tipo': '', 'descripcion': '','numero_folio': '', 'user': '', 'estado': 'Digitalizacion', 
            'flag': '¿ revisión ?'
        }