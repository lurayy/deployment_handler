# Generated by Django 3.1.2 on 2020-10-15 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20201015_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='erp',
            name='has_container',
        ),
        migrations.RemoveField(
            model_name='erp',
            name='is_running',
        ),
    ]
