# Generated by Django 2.1.4 on 2019-01-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_hitcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitcount',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]