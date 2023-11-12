# Generated by Django 4.2.1 on 2023-11-12 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_product_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="category",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="productline",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_line",
                to="product.product",
            ),
        ),
    ]
