# Generated by Django 5.1.2 on 2024-10-10 03:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanmonitoring', '0002_monitoringpersonal'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoringpersonal',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
