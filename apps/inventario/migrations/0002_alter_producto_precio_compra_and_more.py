# Generated by Django 5.1.7 on 2025-03-19 01:05

import data.custom_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto",
            name="precio_compra",
            field=data.custom_fields.CustomMoneyField(verbose_name="Precio Compra"),
        ),
        migrations.AlterField(
            model_name="producto",
            name="precio_venta",
            field=data.custom_fields.CustomMoneyField(verbose_name="Precio Venta"),
        ),
    ]
