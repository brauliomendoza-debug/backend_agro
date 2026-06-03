from django.db import models

class Agricultor(models.Model):
    nombre = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='agricultores/')

    def __str__(self):
        return self.nombre


class ProductoAgricola(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='productos/')
    agricultor = models.ForeignKey(
        Agricultor,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre