from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'tipo', 'color', 'metros_tela', 'stock']
        # 'fecha_creacion' is auto_now_add=True, so it's not included in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_producto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej: Polera Deportiva DryFit'})
        self.fields['tipo'].widget.attrs.update({'class': 'form-select'})
        self.fields['color'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej: Azul Marino'})
        self.fields['metros_tela'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej: 1.5'})
        self.fields['stock'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej: 100'})

        # Example of adding help text if needed
        # self.fields['metros_tela'].help_text = 'Cantidad de tela utilizada en metros.'

        # Example of custom validation if needed
    # def clean_stock(self):
    #     stock = self.cleaned_data.get('stock')
    #     if stock is not None and stock < 0:
    #         raise forms.ValidationError("El stock no puede ser negativo.")
    #     return stock

    # def clean_metros_tela(self):
    #     metros_tela = self.cleaned_data.get('metros_tela')
    #     if metros_tela is not None and metros_tela <= 0:
    #         raise forms.ValidationError("Los metros de tela deben ser un valor positivo.")
    #     return metros_tela
