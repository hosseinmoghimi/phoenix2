# Generated by Django 3.1.2 on 2020-10-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20201022_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='icon',
            name='icon_class',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='کلاس آیکون'),
        ),
    ]