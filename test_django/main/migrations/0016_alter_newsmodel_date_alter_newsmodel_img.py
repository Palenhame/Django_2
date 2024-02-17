# Generated by Django 5.0.1 on 2024-02-11 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_newsmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 11, 17, 23, 1, 603212), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/images_from_user/%Y/%m/%d/'),
        ),
    ]