# Generated by Django 4.2.5 on 2023-12-26 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enviromentalAlert', '0002_alter_environmentalalert_threshold_humidity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environmentalalert',
            name='threshold_humidity',
        ),
        migrations.RemoveField(
            model_name='environmentalalert',
            name='threshold_temperature',
        ),
        migrations.RemoveField(
            model_name='environmentalalert',
            name='threshold_water_quality',
        ),
    ]
