# Generated by Django 5.1.7 on 2025-03-11 02:32

import data.custom_fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Caja",
            fields=[
                (
                    "id",
                    data.custom_fields.CustomAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    data.custom_fields.CustomCharField(
                        max_length=100, verbose_name="Nombre"
                    ),
                ),
                (
                    "fecha_apertura",
                    data.custom_fields.CustomDateTimeField(
                        verbose_name="Fecha Apertura"
                    ),
                ),
                (
                    "fecha_cierre",
                    data.custom_fields.CustomDateTimeField(
                        blank=True, null=True, verbose_name="Fecha Cierre"
                    ),
                ),
                (
                    "monto_apertura",
                    data.custom_fields.CustomIntegerField(
                        verbose_name="Monto Apertura"
                    ),
                ),
                (
                    "monto_cierre",
                    data.custom_fields.CustomIntegerField(
                        blank=True, null=True, verbose_name="Monto Cierre"
                    ),
                ),
                (
                    "activo",
                    data.custom_fields.CustomBooleanField(
                        default=True, verbose_name="Activo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Caja",
                "verbose_name_plural": "Cajas",
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    data.custom_fields.CustomAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo",
                    data.custom_fields.CustomCharField(
                        max_length=10,
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name="Código",
                    ),
                ),
                (
                    "nombre",
                    data.custom_fields.CustomCharField(
                        max_length=100, verbose_name="Nombre"
                    ),
                ),
                (
                    "descripcion",
                    data.custom_fields.CustomCharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
                (
                    "activo",
                    data.custom_fields.CustomBooleanField(
                        default=True, verbose_name="Activo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoría",
                "verbose_name_plural": "Categorías",
            },
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    data.custom_fields.CustomAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    data.custom_fields.CustomCharField(
                        max_length=100, verbose_name="Nombre"
                    ),
                ),
                (
                    "email",
                    data.custom_fields.CustomEmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "activo",
                    data.custom_fields.CustomBooleanField(
                        default=True, verbose_name="Activo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuario",
                "verbose_name_plural": "Usuarios",
            },
        ),
        migrations.CreateModel(
            name="ActividadCaja",
            fields=[
                (
                    "id",
                    data.custom_fields.CustomAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", data.custom_fields.CustomDateTimeField(verbose_name="Fecha")),
                ("monto", data.custom_fields.CustomIntegerField(verbose_name="Monto")),
                (
                    "descripcion",
                    data.custom_fields.CustomCharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
                (
                    "caja",
                    data.custom_fields.CustomForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.caja",
                        verbose_name="Caja",
                    ),
                ),
            ],
            options={
                "verbose_name": "Actividad Caja",
                "verbose_name_plural": "Actividad Cajas",
            },
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    data.custom_fields.CustomAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo",
                    data.custom_fields.CustomCharField(
                        max_length=10,
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name="Código",
                    ),
                ),
                (
                    "nombre",
                    data.custom_fields.CustomCharField(
                        max_length=100, verbose_name="Nombre"
                    ),
                ),
                (
                    "descripcion",
                    data.custom_fields.CustomCharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
                (
                    "precio_compra",
                    data.custom_fields.CustomIntegerField(verbose_name="Precio Compra"),
                ),
                (
                    "precio_venta",
                    data.custom_fields.CustomIntegerField(verbose_name="Precio Venta"),
                ),
                ("stock", data.custom_fields.CustomIntegerField(verbose_name="Stock")),
                (
                    "activo",
                    data.custom_fields.CustomBooleanField(
                        default=True, verbose_name="Activo"
                    ),
                ),
                (
                    "categoria",
                    data.custom_fields.CustomForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="data.categoria",
                        verbose_name="Categoría",
                    ),
                ),
            ],
            options={
                "verbose_name": "Producto",
                "verbose_name_plural": "Productos",
            },
        ),
        migrations.AddField(
            model_name="caja",
            name="usuario_apertura",
            field=data.custom_fields.CustomForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="usuario_apertura",
                to="data.usuario",
                verbose_name="Usuario Apertura",
            ),
        ),
        migrations.AddField(
            model_name="caja",
            name="usuario_cierre",
            field=data.custom_fields.CustomForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="usuario_cierre",
                to="data.usuario",
                verbose_name="Usuario Cierre",
            ),
        ),
        migrations.CreateModel(
            name="Venta",
            fields=[
                (
                    "id",
                    data.custom_fields.CustomAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", data.custom_fields.CustomDateTimeField(verbose_name="Fecha")),
                ("total", data.custom_fields.CustomIntegerField(verbose_name="Total")),
                (
                    "caja",
                    data.custom_fields.CustomForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.caja",
                        verbose_name="Caja",
                    ),
                ),
                (
                    "usuario",
                    data.custom_fields.CustomForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="data.usuario",
                        verbose_name="Usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Venta",
                "verbose_name_plural": "Ventas",
            },
        ),
        migrations.CreateModel(
            name="DetalleVenta",
            fields=[
                (
                    "id",
                    data.custom_fields.CustomAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cantidad",
                    data.custom_fields.CustomIntegerField(verbose_name="Cantidad"),
                ),
                (
                    "precio",
                    data.custom_fields.CustomIntegerField(verbose_name="Precio"),
                ),
                (
                    "producto",
                    data.custom_fields.CustomForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.producto",
                        verbose_name="Producto",
                    ),
                ),
                (
                    "venta",
                    data.custom_fields.CustomForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.venta",
                        verbose_name="Venta",
                    ),
                ),
            ],
            options={
                "verbose_name": "Detalle Venta",
                "verbose_name_plural": "Detalle Ventas",
            },
        ),
    ]
