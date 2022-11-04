from ipaddress import ip_address
from django.db import models
from datetime import datetime , date

# Create your models here.
class Computer(models.Model):
    computer_name = models.CharField(max_length = 50,blank=True)
    ip_address = models.CharField(max_length = 50,blank=True)
    MAC_address = models.CharField(max_length = 50,blank=True)
    username = models.CharField(max_length = 50, blank=True)
    location = models.CharField(max_length = 50,blank=True)
    purchase_date = models.DateField("Purchase date (mm/dd/yyyy)",auto_now_add = False , auto_now = False, blank = True, null=True)
    timestamp = models.DateField(auto_now_add = True , auto_now = False, blank = True)

    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.ip_address + " " + self.computer_name

