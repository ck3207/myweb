# Generated by Django 2.1.8 on 2020-03-11 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0009_auto_20200311_1037'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servers',
            unique_together=set(),
        ),
    ]
