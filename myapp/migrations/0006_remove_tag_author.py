# Generated by Django 3.2.6 on 2021-08-31 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210831_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='author',
        ),
    ]