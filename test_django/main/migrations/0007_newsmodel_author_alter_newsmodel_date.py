# Generated by Django 5.0.1 on 2024-01-29 14:55

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_newsmodel_date_alter_newsmodel_img'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 29, 17, 55, 31, 303955), verbose_name='Date'),
        ),
    ]
