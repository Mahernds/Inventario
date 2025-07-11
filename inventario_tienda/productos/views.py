from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto

# Create your views here.
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new URL: perhaps a list of products or success page
            # For now, redirecting back to the same form, but ideally, you'd redirect elsewhere.
            # Example: return redirect('lista_productos')
            # Or display a success message.
            return redirect('agregar_producto') # Or some success URL
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

# Placeholder for a product list view, if you want to redirect to it after adding a product.
# def lista_productos(request):
#     productos = Producto.objects.all()
#     return render(request, 'productos/lista_productos.html', {'productos': productos})
