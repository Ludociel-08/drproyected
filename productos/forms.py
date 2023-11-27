from django.forms import ModelForm
from .models import Productos, Componentes


class CreateProducto(ModelForm):
    class Meta:
        model = Productos
        fields = ['Modelo', 'Tipo', 'Precio', 'Fecha_Lanzamiento']


class CreateComponentes(ModelForm):
    class Meta:
        model = Componentes
        fields = ['Nombre', 'Descripcion', 'Producto']
