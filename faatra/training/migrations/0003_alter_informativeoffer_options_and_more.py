# Generated by Django 4.0.1 on 2022-02-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_informativeoffer_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informativeoffer',
            options={'verbose_name': 'Oferta formativa', 'verbose_name_plural': 'Oferta formativa'},
        ),
        migrations.AlterField(
            model_name='daterealization',
            name='created_date',
            field=models.DateField(verbose_name='Fecha de creación'),
        ),
    ]