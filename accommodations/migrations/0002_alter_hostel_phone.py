# Generated by Django 4.2.3 on 2023-07-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accommodations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hostel",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
