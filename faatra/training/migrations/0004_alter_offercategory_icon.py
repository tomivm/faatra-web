# Generated by Django 4.0.1 on 2022-05-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_alter_informativeoffer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offercategory',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Imagen'),
        ),
    ]
