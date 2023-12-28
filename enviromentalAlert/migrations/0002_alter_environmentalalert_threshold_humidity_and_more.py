# Generated by Django 4.2.5 on 2023-12-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviromentalAlert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmentalalert',
            name='threshold_humidity',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='environmentalalert',
            name='threshold_temperature',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='environmentalalert',
            name='threshold_water_quality',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]