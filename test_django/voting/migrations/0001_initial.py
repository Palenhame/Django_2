# Generated by Django 5.0.1 on 2024-03-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VotingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('value1', models.CharField(max_length=20)),
                ('value2', models.CharField(max_length=20)),
                ('value3', models.CharField(max_length=20)),
                ('value4', models.CharField(max_length=20)),
                ('value1_votes', models.IntegerField()),
                ('value2_votes', models.IntegerField()),
                ('value3_votes', models.IntegerField()),
                ('value4_votes', models.IntegerField()),
            ],
        ),
    ]
