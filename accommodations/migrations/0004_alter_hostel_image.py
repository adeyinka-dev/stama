# Generated by Django 4.2.3 on 2023-07-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accommodations", "0003_hostel_image_hostel_stama_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hostel",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="hostels/"),
        ),
    ]