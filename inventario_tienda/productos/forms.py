from django import forms
from .models import Producto, TelaDisponible, Color


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'tipo', 'color', 'stock']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_producto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej: Polera Deportiva DryFit'})
        self.fields['tipo'].widget.attrs.update({'class': 'form-select'})
        
        # color como lista desplegable basada en Color
        self.fields['color'].queryset = Color.objects.all()
        self.fields['color'].widget.attrs.update({'class': 'form-select'})
        self.fields['color'].empty_label = "Selecciona un color"
        
        self.fields['stock'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej: 100'})


class TelaDisponibleForm(forms.ModelForm):
    class Meta:
        model = TelaDisponible
        fields = ['nombre', 'color', 'metros_disponibles']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej: Algodón'})
        
        # color como lista desplegable basada en Color
        self.fields['color'].queryset = Color.objects.all()
        self.fields['color'].widget.attrs.update({'class': 'form-select'})
        self.fields['color'].empty_label = "Selecciona un color"
        
        self.fields['metros_disponibles'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej: 10.5'})
