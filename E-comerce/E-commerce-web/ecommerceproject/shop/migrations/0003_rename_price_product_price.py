# Generated by Django 4.1.3 on 2022-11-16 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_availible_product_available_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Price',
            new_name='price',
        ),
    ]
