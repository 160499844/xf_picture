# Generated by Django 2.0.1 on 2020-09-10 02:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PictureItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100, null=True, verbose_name='文件名')),
                ('resource', models.CharField(blank=True, max_length=100, verbose_name='文件夹位置')),
                ('explain', models.TextField(blank=True, null=True, verbose_name='说明')),
                ('status', models.CharField(blank=True, choices=[('E', '生效'), ('F', '失效')], default='E', max_length=10, verbose_name='状态')),
                ('create_dt', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='系统收录时间')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='最后一次操作时间')),
            ],
            options={
                'verbose_name': '相册目录',
                'verbose_name_plural': '相册目录',
            },
        ),
    ]