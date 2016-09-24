# Create your models here.

from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from manager.choices import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentNumber = models.CharField(max_length=30, blank=True)
    idNumber = models.CharField(max_length=30)
    cellphone = models.CharField(max_length=30)
    residence = models.CharField(max_length=30)
    roomNumber = models.CharField(max_length=30)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self): return user.first_name


class MaintenanceType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self): return self.name


class MaintenanceStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self): return self.name


class MaintainerType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): return self.name


class Maintainer(models.Model):
    type = models.ForeignKey(MaintainerType)
    name = models.CharField(max_length=50)

    def __str__(self): return self.name


class MaintananceRequest(models.Model):
    referenceNumber = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=MAINTENACE_TYPE)
    status = models.CharField(max_length=10, choices=MAINTENACE_STATUS_CHOICE)
    description = models.TextField()
    picture = models.ImageField(upload_to='maintenancerequests/', blank=True)
    datelogged = models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(User)
    maintainerId = models.ForeignKey(Maintainer, default=1)
    expirationdate = models.DateTimeField(default=datetime.now() + timedelta(days=7))  # Expire after 7 days

    def __str__(self):
        return self.type + ' request with reference number: ' + self.referenceNumber

class Residence(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self): return self.name

# Use the free Admin page for MaintananceRequests

# Do they want Incidents allocated to specific people?
# separe app : Incident Allocator
