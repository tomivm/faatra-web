# Generated by Django 4.0.1 on 2022-07-01 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incriptions', '0005_alter_incription_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incription',
            name='saloon',
        ),
    ]