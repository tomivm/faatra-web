# Generated by Django 4.0.1 on 2022-01-24 16:43

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, verbose_name='Fecha de creación')),
                ('title', models.CharField(max_length=256, verbose_name='Titulo')),
                ('description', models.CharField(max_length=256, verbose_name='resumen')),
                ('content', django_quill.fields.QuillField()),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('last_modification_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de la ultima publicacion')),
                ('is_available', models.BooleanField(default=False, verbose_name='Habilitado')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
