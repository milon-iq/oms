# Generated by Django 4.1.5 on 2023-01-19 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0017_remove_order_unit_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='products',
        ),
    ]
