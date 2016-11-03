# Create your models here.

from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from manager.choices import *


class Residence(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self): return self.name


class MaintenanceStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self): return self.name


class MaintananceRequest(models.Model):
    referenceNumber = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=MAINTENACE_TYPE)
    status = models.CharField(max_length=30, choices=MAINTENACE_STATUS_CHOICE)
    description = models.TextField()
    picture = models.ImageField(upload_to='maintenancerequests/', blank=True)
    datelogged = models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(User)
    residence = models.ForeignKey(Residence, default=1)
    expirationdate = models.DateTimeField(default=datetime.now() + timedelta(days=7))  # Expire after 7 days

    def __str__(self):
        return self.type + ' request : ' + self.referenceNumber


class ResidenceMaintainer(models.Model):
    residence = models.ForeignKey(Residence)
    maintainer = models.ForeignKey(User)

    def __str__(self): return 'Maintainer number: ' + self.maintainer + ' for residence number: ' + self.residence


class UserType(models.Model):
    name = models.CharField(max_length=10)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personnelNumber = models.CharField(max_length=30, blank=True)
    idNumber = models.CharField(max_length=13)
    cellphone = models.CharField(max_length=10)
    residence = models.ForeignKey(Residence, default=1)
    roomNumber = models.CharField(max_length=30)
    usertype = models.ForeignKey(UserType, default=1)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self): return user.first_name + user.last_name
