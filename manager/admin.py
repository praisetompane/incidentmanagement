from django.contrib import admin
from manager.models import *
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(MaintananceRequest)
admin.site.register(Profile)
admin.site.register(ResidenceMaintainer)
admin.site.register(Residence)




