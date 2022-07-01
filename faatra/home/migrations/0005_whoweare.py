# Generated by Django 4.0.1 on 2022-07-01 14:23

import datetime
from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_socialmediaconfiguration_snit_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoWeAre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, default=datetime.datetime.now, verbose_name='Fecha de creación')),
                ('title', models.CharField(max_length=256, verbose_name='Titulo')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='resumen')),
                ('content', django_quill.fields.QuillField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Imagen')),
                ('last_modification_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de la ultima modificación')),
                ('is_available', models.BooleanField(default=False, verbose_name='Habilitado')),
                ('url', models.SlugField(max_length=256, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Quienes somos',
                'verbose_name_plural': 'Quienes somos',
            },
        ),
    ]