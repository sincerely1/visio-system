# Generated by Django 2.2 on 2022-05-01 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220501_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='ture_name',
            new_name='true_name',
        ),
    ]
