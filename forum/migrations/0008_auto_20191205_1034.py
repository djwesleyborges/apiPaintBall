# Generated by Django 2.2.3 on 2019-12-05 13:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20191205_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
