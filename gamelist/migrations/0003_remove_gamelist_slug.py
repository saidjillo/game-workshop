# Generated by Django 2.1.4 on 2019-01-01 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0002_gamelist_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamelist',
            name='slug',
        ),
    ]