# Generated by Django 2.0.1 on 2020-09-10 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200910_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictureitem',
            name='resource',
            field=models.FilePathField(blank=True, path='D:/broadband_img', recursive=True, verbose_name='文件夹位置'),
        ),
    ]