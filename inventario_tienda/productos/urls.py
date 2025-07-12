from django.urls import path
from . import views

app_name = 'productos'  # Optional: define 

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('tela/', views.stock_tela, name='stock_tela'),
    path('colores/', views.agregar_color, name='agregar_color'),
    path('pedido/', views.hacer_pedido, name='hacer_pedido'),
    path('eliminar/', views.eliminar_productos, name='eliminar_productos'),


]