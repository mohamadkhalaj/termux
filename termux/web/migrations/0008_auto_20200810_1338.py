# Generated by Django 3.1 on 2020-08-10 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200810_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_log',
            name='date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sms_list',
            name='received',
            field=models.CharField(max_length=50),
        ),
    ]
