# Generated by Django 4.0.6 on 2022-10-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_supermarket_alter_product_options_supermarketrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supermarketrow',
            name='place',
            field=models.CharField(max_length=20),
        ),
    ]
