# Generated by Django 4.2.3 on 2023-07-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenant",
            name="stama_id",
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
