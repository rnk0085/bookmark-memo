# Generated by Django 3.2.6 on 2021-08-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210825_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='site_url',
            field=models.CharField(max_length=200, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='タグ'),
        ),
    ]
