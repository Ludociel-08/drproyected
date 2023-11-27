# Generated by Django 4.2.7 on 2023-11-23 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UbicacionAlmacen',
            fields=[
                ('ID_UbicacionAlmacen', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.TextField()),
                ('Descripcion', models.TextField()),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubicacion_almacen', to='productos.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Componentes',
            fields=[
                ('ID_Componente', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.TextField()),
                ('Descripcion', models.TextField()),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentes', to='productos.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('ID_Caracteristica', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.TextField()),
                ('Descripcion', models.TextField()),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caracteristicas', to='productos.productos')),
            ],
        ),
    ]