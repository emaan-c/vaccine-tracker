# Generated by Django 3.2.3 on 2021-05-15 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210515_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={},
        ),
        migrations.RemoveField(
            model_name='information',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='information',
            name='longitude',
        ),
    ]