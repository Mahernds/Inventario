from django.db import models

class Color(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


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
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    metros_tela = models.FloatField()
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto


class TelaDisponible(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    metros_disponibles = models.FloatField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.color}"


class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
