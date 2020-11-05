# Generated by Django 3.1.2 on 2020-11-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_auto_20201105_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='suggestions',
            field=models.ManyToManyField(blank=True, related_name='suggestions_category', to='market.Product', verbose_name='پیشنهاد برای مشتری'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='شرح کوتاه'),
        ),
    ]
