# Generated by Django 2.2.3 on 2019-12-05 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20191205_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.Publication'),
        ),
    ]