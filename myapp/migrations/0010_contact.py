# Generated by Django 3.2.6 on 2021-09-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_post_site_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='お名前')),
                ('mail', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('context', models.TextField(max_length=2000, verbose_name='お問い合わせ内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
            ],
        ),
    ]