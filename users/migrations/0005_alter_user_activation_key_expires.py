# Generated by Django 3.2.8 on 2021-11-14 15:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211111_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 15, 28, 51, 67250, tzinfo=utc)),
        ),
    ]