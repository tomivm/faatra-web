# Generated by Django 4.0.1 on 2022-02-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saloon', '0003_alter_saloon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='saloon',
            name='maps',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Link a google maps'),
        ),
    ]
