# Generated by Django 3.1.2 on 2020-10-22 12:54

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=50, verbose_name='color name')),
                ('color_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='color code')),
                ('color_class', models.CharField(blank=True, choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('', '')], default='', max_length=50, null=True, verbose_name='color class')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50, verbose_name='icon')),
            ],
            options={
                'verbose_name': 'Icon',
                'verbose_name_plural': 'Icons',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Jumbotron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='عنوان')),
                ('pretitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='پیش عنوان')),
                ('posttitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='پس عنوان')),
                ('short_description', tinymce.models.HTMLField(blank=True, max_length=1000, null=True, verbose_name='شرح کوتاه')),
                ('description', tinymce.models.HTMLField(blank=True, max_length=2000, null=True, verbose_name='شرح کامل')),
            ],
            options={
                'verbose_name': 'Jumbotron',
                'verbose_name_plural': 'Jumbotrons',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.color')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.icon')),
                ('jumbotron', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.jumbotron')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]