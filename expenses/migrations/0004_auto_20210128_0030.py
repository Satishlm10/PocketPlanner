# Generated by Django 3.0.1 on 2021-01-27 23:30

import datetime

from django.db import migrations, models
from django.utils import timezone



class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0003_auto_20210128_0029"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="date",
            field=models.DateTimeField(
                default=timezone.now

            ),
        ),

    ]
