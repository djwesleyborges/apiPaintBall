# Generated by Django 2.2.3 on 2019-11-28 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20191128_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='publication',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Publication'),
        ),
    ]