# Generated by Django 4.0.1 on 2022-02-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saloon', '0002_alter_saloon_address_alter_saloon_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saloon',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='resumen'),
        ),
    ]
