# Generated by Django 2.1 on 2018-08-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaperAPI', '0004_auto_20180815_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='获取图片数量')),
                ('imei', models.CharField(max_length=18, verbose_name='imei')),
                ('active_status', models.CharField(choices=[('1', '激活'), ('0', '去激活')], max_length=2)),
                ('address', models.CharField(max_length=500, verbose_name='链接地址')),
            ],
            options={
                'ordering': ['active_status'],
            },
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='获取图片数量')),
                ('page', models.IntegerField(blank=True, null=True, verbose_name='页数')),
                ('active_status', models.CharField(choices=[('1', '激活'), ('0', '去激活')], max_length=2)),
                ('address', models.CharField(max_length=500, verbose_name='链接地址')),
            ],
            options={
                'ordering': ['active_status'],
            },
        ),
    ]
