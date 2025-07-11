from django.urls import path
from . import views

app_name = 'productos' # Optional: define an application namespace

urlpatterns = [
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    # Example for a product list view, if created:
    # path('', views.lista_productos, name='lista_productos'),
]
