# Generated by Django 4.0.1 on 2022-01-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_socialmediaconfiguration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='attention',
            field=models.TextField(max_length=1024, verbose_name='Horario de atencion'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='email',
            field=models.TextField(max_length=1024, verbose_name='Email de contacto'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='location',
            field=models.TextField(max_length=1024, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='phone',
            field=models.TextField(max_length=1024, verbose_name='Número de contacto'),
        ),
        migrations.AlterField(
            model_name='socialmediaconfiguration',
            name='facebook',
            field=models.TextField(max_length=1024, verbose_name='Link a facebook'),
        ),
        migrations.AlterField(
            model_name='socialmediaconfiguration',
            name='instagram',
            field=models.TextField(max_length=1024, verbose_name='Link a instagram'),
        ),
        migrations.AlterField(
            model_name='socialmediaconfiguration',
            name='linkedin',
            field=models.TextField(max_length=1024, verbose_name='Link a linkedin'),
        ),
        migrations.AlterField(
            model_name='socialmediaconfiguration',
            name='twitter',
            field=models.TextField(max_length=1024, verbose_name='Link a twitter'),
        ),
        migrations.AlterField(
            model_name='socialmediaconfiguration',
            name='wsp',
            field=models.TextField(max_length=1024, verbose_name='Link a Whatsapp'),
        ),
        migrations.AlterField(
            model_name='socialmediaconfiguration',
            name='youtube',
            field=models.TextField(max_length=1024, verbose_name='Link a Youtube'),
        ),
    ]
