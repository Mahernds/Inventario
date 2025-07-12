
from django.contrib import admin
from django.urls import path, include # Added include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')), # Added products urls
    path('', lambda request: redirect('productos:lista_productos', permanent=False)),

]
