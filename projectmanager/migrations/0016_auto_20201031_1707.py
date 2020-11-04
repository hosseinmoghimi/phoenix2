# Generated by Django 3.1.2 on 2020-10-31 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0015_auto_20201031_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='percent',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='درصد پیشرفت'),
        ),
    ]