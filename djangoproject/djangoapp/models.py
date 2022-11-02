from ipaddress import ip_address
from django.db import models
from datetime import datetime , date

# Create your models here.
class Computer(models.Model):
    computer_name = models.CharField(max_length = 50)
    ip_address = models.CharField(max_length = 50)
    MAC_address = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    purchase_date = models.DateField("Purchase date (mm/dd/yyyy)",auto_now_add = False , auto_now = False, blank = True, null=True)
    timestamp = models.DateField(auto_now_add = True , auto_now = False, blank = True)

    def __str__(self):
        return self.ip_address + " " + self.computer_name

