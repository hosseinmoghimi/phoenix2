# Generated by Django 3.1.2 on 2020-10-24 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerpage',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectmanager.managerpage', verbose_name='parent'),
        ),
    ]
