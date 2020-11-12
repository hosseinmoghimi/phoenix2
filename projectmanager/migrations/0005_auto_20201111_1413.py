# Generated by Django 3.1.2 on 2020-11-11 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0004_assignment_project_for'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('model', models.CharField(blank=True, max_length=50, null=True, verbose_name='model')),
                ('unit_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='واحد')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials -  متریال ها',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='MaterialBrand',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس اینترتی')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands - برند های متریال',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='MaterialCategory',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
            ],
            options={
                'verbose_name': 'MaterialCategory',
                'verbose_name_plural': 'MaterialCategories - دسته بندی های متریال',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='MaterialObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(blank=True, max_length=200, null=True, verbose_name='serial_no')),
                ('barcode1', models.CharField(blank=True, max_length=200, null=True, verbose_name='barcode1')),
                ('borcode2', models.CharField(blank=True, max_length=200, null=True, verbose_name='barcode2')),
                ('barcode3', models.CharField(blank=True, max_length=200, null=True, verbose_name='barcode3')),
                ('package_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='package_no')),
                ('package_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='package_name')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanager.material', verbose_name='material')),
            ],
            options={
                'verbose_name': 'MaterialObject',
                'verbose_name_plural': 'MaterialObjects- متریال های موجود',
            },
        ),
        migrations.CreateModel(
            name='MaterialWareHouse',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='آدرس')),
            ],
            options={
                'verbose_name': 'MaterialWareHouse',
                'verbose_name_plural': 'MaterialWareHouses - انبار های متریال',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='MaterialPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_no', models.CharField(max_length=50, verbose_name='pack_no')),
                ('material_objects', models.ManyToManyField(to='projectmanager.MaterialObject', verbose_name='material_objects')),
            ],
            options={
                'verbose_name': 'MaterialPackage',
                'verbose_name_plural': 'MaterialPackages - پکیج های متریال',
            },
        ),
        migrations.CreateModel(
            name='MaterialInStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(verbose_name='قفسه')),
                ('col', models.IntegerField(verbose_name='ردیف')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('date_opi', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ opi')),
                ('material_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanager.materialobject', verbose_name='متریال')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanager.materialwarehouse', verbose_name='انبار متریال')),
            ],
            options={
                'verbose_name': 'MaterialInStock',
                'verbose_name_plural': 'MaterialInStocks- متریال های موجود در انبار',
            },
        ),
        migrations.AddField(
            model_name='material',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectmanager.materialbrand', verbose_name='brand'),
        ),
        migrations.AddField(
            model_name='material',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='material_category', to='projectmanager.materialcategory'),
        ),
    ]