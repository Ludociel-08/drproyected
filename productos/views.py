from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateProducto, CreateComponentes
from .models import Productos, Componentes
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from .serializers import ProductosSerializer


from django.http import JsonResponse
from django.views import View
from django.db.models import Count
from .models import Productos
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register users
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('productos')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })


@login_required
def productos(request):
    productos = Productos.objects.filter(user=request.user)
    return render(request, 'productos.html', {'productos': productos})


@login_required
def create_productos(request):
    if request.method == 'GET':
        return render(request, 'create_productos.html', {
            'form': CreateProducto
        })
    else:
        try:
            form = CreateProducto(request.POST)
            nuevo_producto = form.save(commit=False)
            nuevo_producto.user = request.user
            nuevo_producto.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'create_productos.html', {
                'form': CreateProducto,
                'error': 'Please provide valida data'
            })


def product_detail(request, id):
    producto = get_object_or_404(Productos, pk=id)
    return render(request, 'product_details.html', {'producto': producto})


def components(request):
    componentes = Componentes.objects.all()
    return render(request, 'componentes.html', {'componentes': componentes})


def create_components(request):
    if request.method == 'GET':
        return render(request, 'create_components.html', {'form': CreateComponentes()})
    elif request.method == 'POST':
        form = CreateComponentes(request.POST)
        if form.is_valid():
            new_componente = form.save(commit=False)
            new_componente.save()
            # Assuming 'components' is the name of your view or URL pattern
            return redirect('components')
        else:
            # If the form is not valid, you may want to handle the error, e.g., redisplay the form with error messages
            return render(request, 'create_components.html', {'form': form})


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('productos')


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer


class TipoProductosDataView(View):
    def get(self, request, *args, **kwargs):
        # Obtén los datos desde la base de datos
        tipos_productos_data = Productos.objects.values(
            'Tipo').annotate(cantidad=Count('Tipo'))

        # Formatea los datos para la gráfica
        tipo_productos_data = [
            {'tipo': item['Tipo'], 'cantidad': item['cantidad']} for item in tipos_productos_data]

        return JsonResponse(tipo_productos_data, safe=False)
