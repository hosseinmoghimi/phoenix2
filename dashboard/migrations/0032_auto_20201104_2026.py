# Generated by Django 3.1.2 on 2020-11-04 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('dashboard', '0031_auto_20201030_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumecategory',
            name='our_team',
        ),
        migrations.AddField(
            model_name='resumecategory',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='profile'),
            preserve_default=False,
        ),
    ]