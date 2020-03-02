# Generated by Django 3.0.2 on 2020-02-01 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200201_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 11, 27, 19, 360848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique_for_date=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 11, 27, 19, 360848, tzinfo=utc))),
        ),
    ]