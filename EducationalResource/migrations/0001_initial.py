# Generated by Django 4.2.5 on 2023-12-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'EducationalResources',
            },
        ),
    ]
