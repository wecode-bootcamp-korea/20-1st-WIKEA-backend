# Generated by Django 3.2.2 on 2021-05-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_backgorund_image_product_background_image'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='backgroundimage',
            table='background_images',
        ),
    ]