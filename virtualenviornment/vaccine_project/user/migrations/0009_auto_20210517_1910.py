# Generated by Django 3.2.3 on 2021-05-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210517_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='brampton',
            name='latitude',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='brampton',
            name='longitude',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='hamilton',
            name='latitude',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='hamilton',
            name='longitude',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='mississauga',
            name='latitude',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='mississauga',
            name='longitude',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='ottawa',
            name='latitude',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='ottawa',
            name='longitude',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
