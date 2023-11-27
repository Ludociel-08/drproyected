from django.contrib import admin
from .models import Productos
from .models import Componentes
from .models import Caracteristicas
from .models import UbicacionAlmacen

# Register your models here.
admin.site.register(Productos)
admin.site.register(Componentes)
admin.site.register(Caracteristicas)
admin.site.register(UbicacionAlmacen)
