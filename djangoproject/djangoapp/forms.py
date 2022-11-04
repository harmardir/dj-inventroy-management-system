from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
  class Meta:
       model = Computer
       fields = ['computer_name','ip_address','MAC_address','username','location','purchase_date']
  
  def clean_computer_name(self):
    computer_name = self.cleaned_data.get("computer_name")
    if (computer_name == ""):
      raise forms.ValidationError("This field cannot be left blank")
    for instance in Computer.objects.all():
      if instance.computer_name == computer_name:
        raise forms.ValidationError('There is a computer with the name ' + computer_name)
    return computer_name
  
  def clean_ip_address(self):
    ip_address = self.cleaned_data.get("ip_address")
    if (ip_address == ""):
      raise forms.ValidationError("This field cannot be left blank")
    for instance in Computer.objects.all():
      if instance.ip_address == ip_address:
        raise forms.ValidationError('There is a computer with the name ' + ip_address)
    return ip_address


class ComputerSearchForm(forms.ModelForm):
  class Meta:
    model = Computer
    fields = ['computer_name','username', 'export_to_CSV']