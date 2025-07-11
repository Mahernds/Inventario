from django.db import models

class Producto(models.Model):
    TIPO_PRODUCTO = [
        ('polera_hombre', 'Polera Hombre'),
        ('polera_mujer', 'Polera Mujer'),
        ('short', 'Short'),
        ('falda', 'Falda'),
        ('poleron', 'Polerón'),
    ]

    nombre_producto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_PRODUCTO)
    color = models.CharField(max_length=50)
    metros_tela = models.FloatField()
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto
