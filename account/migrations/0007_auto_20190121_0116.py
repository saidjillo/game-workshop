# Generated by Django 2.1.4 on 2019-01-20 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20190121_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.ImageField(blank=True, upload_to='account/%Y/%m/%d'),
        ),
    ]
