# Generated by Django 3.1.2 on 2020-11-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0002_assignment_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('سرپرست', 'سرپرست'), ('نگهبان', 'نگهبان'), ('مدیر', 'مدیر'), ('فنی', 'فنی'), ('تایید نشده', 'تایید نشده'), ('حسابدار', 'حسابدار'), ('صندوقدار', 'صندوقدار')], default='تایید نشده', max_length=50, verbose_name='نقش'),
        ),
    ]
