# Generated by Django 4.2.3 on 2023-08-13 17:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("maintenance", "0009_note"),
    ]

    operations = [
        migrations.RenameField(
            model_name="note",
            old_name="comment",
            new_name="note",
        ),
    ]
