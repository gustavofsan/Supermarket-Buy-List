# Generated by Django 4.0.6 on 2022-10-06 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_alter_supermarketrow_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupermarketProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='place',
        ),
        migrations.DeleteModel(
            name='SupermarketRow',
        ),
        migrations.AddField(
            model_name='supermarketproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.product'),
        ),
        migrations.AddField(
            model_name='supermarketproduct',
            name='supermarket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.supermarket'),
        ),
    ]
