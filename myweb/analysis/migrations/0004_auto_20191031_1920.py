# Generated by Django 2.1.8 on 2019-10-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_auto_20191031_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labledetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='labledetail',
            name='table_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
