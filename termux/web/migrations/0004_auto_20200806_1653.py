# Generated by Django 3.1 on 2020-08-06 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='call_log',
        ),
        migrations.DeleteModel(
            name='clipboard',
        ),
        migrations.DeleteModel(
            name='contact_list',
        ),
        migrations.DeleteModel(
            name='sms_list',
        ),
        migrations.DeleteModel(
            name='token',
        ),
    ]
