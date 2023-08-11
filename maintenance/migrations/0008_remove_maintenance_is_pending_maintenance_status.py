# Generated by Django 4.2.3 on 2023-08-11 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("maintenance", "0007_alter_maintenance_subtype"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="maintenance",
            name="is_pending",
        ),
        migrations.AddField(
            model_name="maintenance",
            name="status",
            field=models.CharField(
                choices=[
                    ("P", "Pending"),
                    ("WP", "In_Progress"),
                    ("INP", "Pending_Inspection"),
                    ("C", "Completed"),
                ],
                default="P",
                max_length=20,
            ),
        ),
    ]
