# Generated by Django 3.1.2 on 2020-11-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0010_materialrequestsignature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='category',
        ),
        migrations.AlterField(
            model_name='materialrequestsignature',
            name='status',
            field=models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('تحویل شده', 'تحویل شده'), ('در حال بررسی', 'درحال بررسی'), ('رد شده', 'ردشده'), ('پذیرفته شده', 'پذیرفته شده'), ('درحال خرید', 'درحال خرید')], default='DEFAULT', max_length=200, verbose_name='status'),
        ),
    ]
