# Generated by Django 2.2.1 on 2020-09-13 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200913_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertoken',
            name='folder_item_id',
        ),
        migrations.AddField(
            model_name='usertoken',
            name='folder_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folderItemFK', to='app.FolderItem', verbose_name='允许访问'),
        ),
    ]
