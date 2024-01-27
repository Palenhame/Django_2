# Generated by Django 5.0 on 2024-01-27 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_newsmodel_date_alter_newsmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 16, 51, 13, 170900), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='img',
            field=models.ImageField(upload_to='static/images_from_user/%Y/%m/%d/'),
        ),
    ]
