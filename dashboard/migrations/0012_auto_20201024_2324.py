# Generated by Django 3.1.2 on 2020-10-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20201024_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeslider',
            name='body',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='بدنه'),
        ),
    ]