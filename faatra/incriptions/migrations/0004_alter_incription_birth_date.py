# Generated by Django 4.0.1 on 2022-07-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incriptions', '0003_alter_incription_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incription',
            name='birth_date',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
    ]
