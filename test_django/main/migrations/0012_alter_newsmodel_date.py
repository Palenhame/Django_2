# Generated by Django 5.0.1 on 2024-02-03 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_newsmodel_date_alter_newsmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 16, 50, 10, 678605), verbose_name='Date'),
        ),
    ]
