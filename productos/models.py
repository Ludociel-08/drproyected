from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Productos(models.Model):
    ID_Producto = models.AutoField(primary_key=True)
    Modelo = models.TextField()
    Tipo = models.TextField()
    Precio = models.FloatField()
    Fecha_Lanzamiento = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Modelo + '- by' + self.user.username


class Componentes(models.Model):
    ID_Componente = models.AutoField(primary_key=True)
    Nombre = models.TextField()
    Descripcion = models.TextField()
    Producto = models.ForeignKey(
        Productos, on_delete=models.CASCADE, related_name='componentes')

    def __str__(self):
        return self.Nombre


class Caracteristicas(models.Model):
    ID_Caracteristica = models.AutoField(primary_key=True)
    Nombre = models.TextField()
    Descripcion = models.TextField()
    Producto = models.ForeignKey(
        Productos, on_delete=models.CASCADE, related_name='caracteristicas')

    def __str__(self):
        return f"{self.Nombre} para {self.Producto.Modelo}"


class UbicacionAlmacen(models.Model):
    ID_UbicacionAlmacen = models.AutoField(primary_key=True)
    Nombre = models.TextField()
    Descripcion = models.TextField()
    Producto = models.ForeignKey(
        Productos, on_delete=models.CASCADE, related_name='ubicacion_almacen')

    def __str__(self):
        return f"Ubicación de almacenamiento para {self.Producto.Modelo}"
