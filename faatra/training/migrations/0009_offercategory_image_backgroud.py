# Generated by Django 4.0.1 on 2022-12-31 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0008_mode_informativeoffer_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='offercategory',
            name='image_backgroud',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Imagen de fondo'),
        ),
    ]
