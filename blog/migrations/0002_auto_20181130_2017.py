# Generated by Django 2.1.3 on 2018-12-01 04:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 1, 4, 17, 32, 963172, tzinfo=utc)),
        ),
    ]
