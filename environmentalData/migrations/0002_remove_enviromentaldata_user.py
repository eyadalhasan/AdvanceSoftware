# Generated by Django 4.2.5 on 2023-12-13 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('environmentalData', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enviromentaldata',
            name='user',
        ),
    ]