# Generated by Django 4.0.1 on 2022-07-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_new_course_alter_new_saloon'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='use_in_home',
            field=models.BooleanField(default=False, verbose_name='Usar en la pagina principal'),
        ),
    ]
