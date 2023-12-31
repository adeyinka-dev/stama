# Generated by Django 4.2.3 on 2023-08-06 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("maintenance", "0004_remove_maintenance_hostel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="maintenance",
            name="subtype",
        ),
        migrations.AddField(
            model_name="maintenancetype",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subtypes",
                to="maintenance.maintenancetype",
            ),
        ),
        migrations.DeleteModel(
            name="MaintenanceSubType",
        ),
    ]
