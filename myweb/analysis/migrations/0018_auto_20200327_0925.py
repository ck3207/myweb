# Generated by Django 2.1.8 on 2020-03-27 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0017_configtable_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configtable',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]