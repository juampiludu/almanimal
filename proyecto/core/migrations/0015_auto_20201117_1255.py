# Generated by Django 3.0.8 on 2020-11-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20201116_1821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AlterModelOptions(
            name='paginadonaciones',
            options={'verbose_name_plural': 'Página donaciones'},
        ),
        migrations.AlterModelOptions(
            name='paginainicio',
            options={'verbose_name_plural': 'Página inicio'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='answered',
            field=models.BooleanField(default=False, verbose_name='Contestado'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_category',
            field=models.CharField(choices=[('CONSULTA', 'Consulta'), ('SUGERENCIA', 'Sugerencia'), ('URGENTE', 'Urgente'), ('DONACIONES', 'Donaciones'), ('OFERTA', 'Oferta'), ('OTRO', 'Otro')], default='CONSULTA', max_length=10, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha'),
        ),
    ]
