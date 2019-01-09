# Generated by Django 2.1.4 on 2019-01-09 20:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('game', '0005_auto_20190109_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2019, 1, 9, 20, 59, 30, 826940, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, related_name='users', to='account.Member'),
            preserve_default=False,
        ),
    ]