# Generated by Django 2.1.5 on 2019-02-20 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_auto_20190220_0917'),
        ('user', '0002_auto_20190219_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.AddField(
            model_name='user',
            name='perfil',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.Perfil'),
        ),
    ]
