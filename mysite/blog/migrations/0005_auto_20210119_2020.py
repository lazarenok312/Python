# Generated by Django 3.1.5 on 2021-01-19 14:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210119_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 14, 20, 49, 743097, tzinfo=utc), verbose_name='publishing date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 14, 20, 49, 742095, tzinfo=utc), verbose_name='publishing date'),
        ),
    ]
