from djmoney.models.fields import MoneyField
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from accommodations.models import Room
from django.urls import reverse
import random


""" Instead of hardcoding different types and subtypes of repair, I created a general and """
""" seperate models for them linking them with foreign keys"""
""" I can then easily add the various types of repairs on the admin page"""


# This model represents the primary type of maintenance, for example, Electrical, Plumbing, carpentry etc.


class MaintenanceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# This model represents the subtype of maintenance, for example, under "Electrical" you might have "Socket", "Light", etc.


class MaintenanceSubType(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        MaintenanceType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subtypes",
    )

    def __str__(self):
        return self.name


# The actual model which is associated with each room and shows the tye of repair needed


class Maintenance(models.Model):
    # Work status to be divided into 3 ,
    PENDING = "P"
    INPROGRESS = "WP"
    INSPECTION = "INP"
    COMPLETED = "C"
    WORK_STATUS = [
        (PENDING, "Pending"),
        (INPROGRESS, "Work In Progress"),
        (INSPECTION, "Inspection"),
        (COMPLETED, "Completed"),
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="repairs")
    location = models.CharField(max_length=20, null=True, blank=True)
    type = models.ForeignKey(
        MaintenanceType, on_delete=models.CASCADE, related_name="repairs"
    )
    time_created = models.DateTimeField(auto_now_add=True)
    subtype = models.ForeignKey(
        MaintenanceSubType,
        on_delete=models.CASCADE,
        related_name="repairs",
        null=True,
        blank=True,
    )

    repair_id = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
    )
    contact = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=WORK_STATUS, default=PENDING)
    description = models.TextField(blank=True, null=True)
    cost = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", null=True
    )

    # Returns the Hostel name associated with the Room of the Maintenance.
    @property
    def hostel(self):
        return self.room.hostel

    def __str__(self):
        return self.repair_id

    # generate url for each repair
    def get_absolute_url(self):
        return reverse("work_detail", args=[str(self.pk)])


# Funtion to generate a repair unique ID, that will be used for repair search.
@receiver(post_save, sender=Maintenance)
def create_repair_id(sender, instance, created, **kwargs):
    if created and not instance.repair_id:
        random_num = f"{random.randint(1, 1000):04}"
        instance.repair_id = "REP" + random_num
        instance.save()


class Note(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    note = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note

    def get_absolute_url(self):
        return reverse("repair_detail")
