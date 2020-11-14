# Generated by Django 3.1.2 on 2020-11-14 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20201107_1439'),
        ('leopusher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن پیام')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('channelevent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leopusher.pusherchannelevent', verbose_name='کانال')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
