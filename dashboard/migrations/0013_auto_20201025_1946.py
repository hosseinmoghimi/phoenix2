# Generated by Django 3.1.2 on 2020-10-25 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20201024_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='documents',
            field=models.ManyToManyField(blank=True, related_name='pages', to='dashboard.Document', verbose_name='پاسخ ها'),
        ),
        migrations.AddField(
            model_name='page',
            name='links',
            field=models.ManyToManyField(blank=True, related_name='pages', to='dashboard.Link', verbose_name='لینک ها'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('image_header', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Tag/', verbose_name='تصویر سربرگ')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.icon', verbose_name='آیکون')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'برچسب ها',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='pages', to='dashboard.Tag', verbose_name='برچسب ها'),
        ),
    ]