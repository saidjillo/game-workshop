# Generated by Django 2.1.4 on 2019-01-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190120_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.ImageField(upload_to='account'),
        ),
    ]