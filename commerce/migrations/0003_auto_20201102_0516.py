# Generated by Django 3.1.2 on 2020-11-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0002_auto_20201101_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitary_price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
