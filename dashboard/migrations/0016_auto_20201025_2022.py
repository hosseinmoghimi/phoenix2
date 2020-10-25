# Generated by Django 3.1.2 on 2020-10-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20201025_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhoto2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Gallery/Photo/Thumbnail/', verbose_name='Thumbnail Image')),
                ('image_origin', models.ImageField(upload_to='dashboard/images/Gallery/Photo/', verbose_name='Big Image 345*970 ')),
                ('archive', models.BooleanField(default=False, verbose_name='Archive?')),
                ('priority', models.IntegerField(default=100, verbose_name='Priority')),
            ],
            options={
                'verbose_name': 'GalleryPhoto',
                'verbose_name_plural': 'تصاویر',
            },
        ),
        migrations.RemoveField(
            model_name='galleryalbum',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='page',
            name='images',
        ),
        migrations.DeleteModel(
            name='GalleryPhoto',
        ),
    ]
