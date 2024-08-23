# Generated by Django 5.1 on 2024-08-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_name', models.CharField(max_length=255, unique=True, verbose_name='برند')),
                ('name', models.CharField(max_length=255, verbose_name='نام نمایشی')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='آخرین آپدیت')),
            ],
        ),
    ]
