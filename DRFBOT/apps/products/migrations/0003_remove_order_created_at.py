# Generated by Django 4.2.5 on 2023-09-24 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
    ]
