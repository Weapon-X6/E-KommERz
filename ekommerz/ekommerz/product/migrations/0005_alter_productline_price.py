# Generated by Django 4.2.1 on 2023-06-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_product_is_active_productline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productline",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]