# Generated by Django 3.1 on 2020-08-06 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sms_list',
            name='duration',
        ),
    ]
