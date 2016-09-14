
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IncidentType(models.Model):
    name = models.CharField(max_length=10)

class MaintainerType(models.Model):
    name = models.CharField(max_length=50)

#class User(models.Model):
#    studentNumber = models.CharField(max_length=15)
#    name = models.CharField(max_length=50)

class Maintainer(models.Model):
    maintainerType = models.ForeignKey(MaintainerType)
    name = models.CharField(max_length=50)

class Incident(models.Model):
    datelogged = models.DateTimeField()
    desciption = models.TextField()
    userid = models.ForeignKey(User)
    maintainerid = models.ForeignKey(Maintainer)
    incidentType = models.ForeignKey(IncidentType)

# Use the free Admin page for administering Incidents

# Do they want Incidents allocated to specific people?
    # separe app : Incident Allocator

