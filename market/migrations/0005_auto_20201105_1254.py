# Generated by Django 3.1.2 on 2020-11-05 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_category_image_header_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_header',
        ),
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
