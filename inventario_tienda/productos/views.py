from django.shortcuts import render, redirect
from .forms import ProductoForm, TelaDisponibleForm
from .models import Producto, TelaDisponible, Color
from django import forms
from django.forms import modelformset_factory
from django.forms import Form, ModelChoiceField, IntegerField
from django.views.decorators.csrf import csrf_protect

# Tela necesaria por tipo de prenda
TELA_POR_TIPO = {
    'short': 4,
    'polera_hombre': 2,
    'polera_mujer': 1.8,
    'falda': 2.5,
    'poleron': 3.5,
}

# Agregar producto con tela automática
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.metros_tela = TELA_POR_TIPO.get(producto.tipo, 0)
            producto.save()
            return redirect('productos:lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

# Mostrar lista de productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

# Agregar, actualizar y eliminar tela disponible
def stock_tela(request):
    telas = TelaDisponible.objects.all()

    if request.method == 'POST':
        # Eliminar tela
        if 'eliminar_tela_id' in request.POST:
            tela_id = request.POST.get('eliminar_tela_id')
            TelaDisponible.objects.filter(id=tela_id).delete()
            return redirect('productos:stock_tela')

        # Actualizar tela existente
        elif 'tela_id' in request.POST:
            tela_id = request.POST.get('tela_id')
            metros_extra = float(request.POST.get('metros_extra', 0))
            tela = TelaDisponible.objects.get(id=tela_id)
            tela.metros_disponibles += metros_extra
            tela.save()
            return redirect('productos:stock_tela')

        # Agregar nueva tela
        else:
            form = TelaDisponibleForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                color = form.cleaned_data['color']
                metros = form.cleaned_data['metros_disponibles']

                tela_existente = TelaDisponible.objects.filter(nombre=nombre, color=color).first()
                if tela_existente:
                    tela_existente.metros_disponibles += metros
                    tela_existente.save()
                else:
                    form.save()
                return redirect('productos:stock_tela')
    else:
        form = TelaDisponibleForm()

    return render(request, 'productos/stock_tela.html', {'form': form, 'telas': telas})

# Formulario para agregar nuevos colores
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['nombre']

# Vista para agregar nuevos colores
def agregar_color(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:agregar_color')
    else:
        form = ColorForm()

    colores = Color.objects.all()
    return render(request, 'productos/agregar_color.html', {'form': form, 'colores': colores})

class PedidoForm(Form):
    producto = ModelChoiceField(queryset=Producto.objects.all(), label="Producto")
    cantidad = IntegerField(min_value=1, label="Cantidad a producir")

def hacer_pedido(request):
    productos = Producto.objects.all()
    form = PedidoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        producto = form.cleaned_data['producto']
        cantidad = form.cleaned_data['cantidad']

        # Más adelante: lógica para descontar tela y verificar stock
        return redirect('productos:hacer_pedido')

    return render(request, 'productos/hacer_pedido.html', {'form': form, 'productos': productos})

@csrf_protect
def eliminar_productos(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        Producto.objects.filter(id=producto_id).delete()
        return redirect('productos:eliminar_productos')
    
    productos = Producto.objects.all()
    return render(request, 'productos/eliminar_productos.html', {'productos': productos})
