# Generated by Django 4.0.1 on 2022-01-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1024, verbose_name='Dirección')),
                ('phone', models.CharField(max_length=1024, verbose_name='Número de contacto')),
                ('email', models.CharField(max_length=1024, verbose_name='Email de contacto')),
                ('attention', models.CharField(max_length=1024, verbose_name='Horario de atencion')),
            ],
            options={
                'verbose_name': 'Faatra configuraciónes',
            },
        ),
    ]
