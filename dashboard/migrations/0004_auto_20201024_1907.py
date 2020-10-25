# Generated by Django 3.1.2 on 2020-10-24 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20201024_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='UNSET', max_length=50, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='color',
            field=models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='UNSET', max_length=50, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='color',
            field=models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='UNSET', max_length=50, verbose_name='رنگ'),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]