# Generated by Django 2.2.3 on 2019-07-22 17:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('complement', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=9)),
                ('price', models.CharField(max_length=8)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='', upload_to='media/%Y/%m/%d/', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created on: ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update on: ')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisements',
                'ordering': ['title'],
            },
        ),
    ]
