# Generated by Django 4.1.5 on 2023-01-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0014_remove_cart_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
