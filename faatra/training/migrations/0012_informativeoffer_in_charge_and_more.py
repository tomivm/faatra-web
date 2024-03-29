# Generated by Django 4.0.1 on 2023-02-27 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0011_alter_informativeoffer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='informativeoffer',
            name='in_charge',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Instructor a cargo'),
        ),
        migrations.AlterField(
            model_name='informativeoffer',
            name='mode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='training.mode', verbose_name='Modalidad'),
        ),
    ]
