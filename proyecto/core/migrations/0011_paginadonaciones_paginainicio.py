# Generated by Django 3.0.8 on 2020-11-16 16:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201110_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaginaDonaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_description', ckeditor.fields.RichTextField(verbose_name='Texto')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
            ],
        ),
        migrations.CreateModel(
            name='PaginaInicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_description', ckeditor.fields.RichTextField(verbose_name='Texto')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
            ],
        ),
    ]
