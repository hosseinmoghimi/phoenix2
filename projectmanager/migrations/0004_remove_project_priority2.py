# Generated by Django 3.1.2 on 2020-10-24 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0003_auto_20201024_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='priority2',
        ),
    ]
