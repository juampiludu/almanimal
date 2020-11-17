# Generated by Django 3.0.8 on 2020-11-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0004_auto_20201117_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email de contacto'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name='Teléfono de contacto'),
        ),
    ]