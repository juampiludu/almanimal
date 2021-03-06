# Generated by Django 3.0.8 on 2020-08-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('tipo_animal', models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')], max_length=40, verbose_name='Tipo de animal')),
                ('raza', models.CharField(max_length=255, verbose_name='Raza')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra'), ('Indefinido', 'Indefinido')], max_length=40, verbose_name='Sexo')),
                ('carácter', models.TextField(blank=True, null=True, verbose_name='Caracter')),
                ('rabia', models.BooleanField(verbose_name='Rabia')),
                ('desparasitados', models.BooleanField(verbose_name='Desparacitado')),
                ('castracion', models.BooleanField(verbose_name='Castración')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentarios')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
            ],
        ),
    ]
