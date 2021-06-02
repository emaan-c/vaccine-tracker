# Generated by Django 3.2.3 on 2021-05-17 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210515_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='brampton',
            name='distance_from_user',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='hamilton',
            name='distance_from_user',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='mississauga',
            name='distance_from_user',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='ottawa',
            name='distance_from_user',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='toronto',
            name='distance_from_user',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
