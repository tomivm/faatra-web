# Generated by Django 4.0.1 on 2023-02-27 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_new_banner_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de creación'),
        ),
    ]
