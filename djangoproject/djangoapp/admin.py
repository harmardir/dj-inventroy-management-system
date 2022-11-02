from django.contrib import admin

from .models import Computer
from .forms import ComputerForm

class ComputerAdmin(admin.ModelAdmin):
    list_display = ["computer_name","ip_address","username","MAC_address","purchase_date","timestamp"]
    form = ComputerForm
    list_filter = ['computer_name','ip_address']
    search_fields = ['computer_name','ip_address','MAC_address']


admin.site.register(Computer,ComputerAdmin)
