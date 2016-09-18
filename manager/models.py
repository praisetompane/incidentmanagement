# Create your models here.

from django.contrib.auth.models import User
from django.db import models

from manager.choices import MAINTENANCE_STATUS_CHOICES, MAINTENANCE_TYPE_CHOICES


# TODO extend the user class with the additional fields (student number, residence etc)
# Create your models here.
class MaintenanceType(models.Model):
    name = models.CharField(max_length=10)


class MaintainerType(models.Model):
    name = models.CharField(max_length=50)


class Maintainer(models.Model):
    maintainerType = models.ForeignKey(MaintainerType)
    name = models.CharField(max_length=50)


class MaintenanceStatus(models.Model):
    name = models.CharField(max_length=30)


class MaintananceRequest(models.Model):
    maintenanceType = models.ForeignKey(MaintenanceType, choices=MAINTENANCE_TYPE_CHOICES)
    status = models.ForeignKey(MaintenanceStatus, choices=MAINTENANCE_STATUS_CHOICES)
    desciption = models.TextField()
    userid = models.ForeignKey(User)
    maintainerid = models.ForeignKey(Maintainer)
    picture = models.BinaryField
    datelogged = models.DateTimeField(auto_now_add=True)

# Use the free Admin page for MaintananceRequests

# Do they want Incidents allocated to specific people?
# separe app : Incident Allocator
