# Generated by Django 4.2.3 on 2023-07-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_tenant_matric_num_alter_tenant_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenant",
            name="middle_initial",
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name="tenant",
            name="first_name",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="tenant",
            name="last_name",
            field=models.CharField(max_length=150),
        ),
    ]
