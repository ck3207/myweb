# Generated by Django 2.1.8 on 2019-10-31 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_id', models.IntegerField(auto_created=True)),
                ('table_name', models.CharField(max_length=128)),
                ('table_num', models.CharField(max_length=128)),
                ('fund_account', models.CharField(max_length=16)),
                ('extreme_value', models.CharField(max_length=512)),
                ('extreme_type', models.IntegerField()),
                ('interval_type', models.IntegerField()),
            ],
        ),
    ]
