# Generated by Django 4.2.3 on 2023-07-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accommodations", "0006_hostel_room_count_room"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hostel",
            name="room_count",
            field=models.IntegerField(default=0),
        ),
    ]