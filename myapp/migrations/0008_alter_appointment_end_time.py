# Generated by Django 4.1 on 2023-12-02 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_appointment_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
