from ipaddress import ip_address
from django.db import models

# Create your models here.
class Computer(models.Model):
    computer_name = models.CharField(max_length = 50)
    ip_address = models.CharField(max_length = 50)
    MAC_address = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)

    def __str__(self):
        return self.ip_address + " " + self.computer_name

