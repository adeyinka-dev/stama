from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
import random


# The user model with additional information
class Tenant(AbstractUser):
    username = models.CharField(max_length=150, unique=True, help_text="")
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1, null=True)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(null=True, blank=True)
    matric_num = models.CharField(max_length=10, unique=True)
    sex = models.CharField(max_length=1)
    faculty = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    level = models.SmallIntegerField(null=True, blank=True)
    # A STAMA id , unique ID generated by random assigned to each tenant.
    stama_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    user_image = models.ImageField(upload_to="users/", null=True, blank=True)

    # Function to return age after user enters there dob
    def age(self):
        today = date.today()
        if self.dob:
            if self.dob > today:
                return "Invalid, Time traveller from the future not allowed!"
            else:
                return (
                    today.year
                    - self.dob.year
                    - ((today.month, today.day) < (self.dob.month, self.dob.day))
                )
        else:
            return None


# Function to generate a unique STAMA_ID , assigned to each user on registration. This is will serve as login later.
# The @receiver decorator inidctaes the function should run when a tenant instance is saved
@receiver(post_save, sender=Tenant)
def create_stama_id(sender, instance, created, **kwargs):
    # If a new Tenant instance has been created and the "stama_id" is empty
    if created and not instance.stama_id:
        # Random number between 1 and 9999
        # The resulting integer is formatted as a string, with leading zeros if necessary to ensure it's 5 digits long
        random_num = f"{random.randint(1, 99999):05}"
        instance.stama_id = "STAMA" + random_num
        instance.save()
