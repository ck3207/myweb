# Generated by Django 2.1.8 on 2020-03-11 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0008_servers'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servers',
            unique_together={('address', 'port', 'user')},
        ),
    ]