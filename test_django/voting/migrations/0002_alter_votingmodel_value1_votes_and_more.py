# Generated by Django 5.0.1 on 2024-03-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votingmodel',
            name='value1_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='votingmodel',
            name='value2_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='votingmodel',
            name='value3_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='votingmodel',
            name='value4_votes',
            field=models.IntegerField(default=0),
        ),
    ]
