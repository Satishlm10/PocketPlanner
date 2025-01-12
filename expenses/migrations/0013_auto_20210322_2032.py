# Generated by Django 3.0.1 on 2021-03-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0012_auto_20210319_1248"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.CharField(
                choices=[
                    ("Bar tabs", "Bar tabs"),
                    ("Electronic", "Electronic"),
                    ("Groceries", "Groceries"),
                    ("Miscellaneous", "Miscellaneous"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]