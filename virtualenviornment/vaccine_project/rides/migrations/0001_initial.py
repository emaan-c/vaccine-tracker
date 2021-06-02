# Generated by Django 3.2.3 on 2021-05-18 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UberInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('postalcode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=6)),
            ],
        ),
    ]
