# Generated by Django 3.0.8 on 2020-11-03 14:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200820_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=ckeditor.fields.RichTextField(verbose_name='Texto'),
        ),
    ]
