# Generated by Django 3.2.3 on 2021-05-15 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210515_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamilton',
            name='vaccine2',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]