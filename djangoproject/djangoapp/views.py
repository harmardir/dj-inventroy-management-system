from django.shortcuts import render , redirect
from djangoapp.forms import ComputerForm , ComputerSearchForm
from .models import Computer
from django.http import HttpResponse
import csv

def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title":title,
    }
    return render(request , "home.html", context)

def computer_entry(request):
    title = 'Add Computer'
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/computer_list')
    context = {
        "title": title,
        "form": form,
    }
    return render(request , "computer_entry.html", context)


def computer_list(request):
    title = 'List of all computers'
    queryset = Computer.objects.all()
    form = ComputerSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Computer.objects.all().order_by('timestamp').filter(computer_name__icontains=form['computer_name'].value() , username__icontains=form['username'].value())
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if form['export_to_CSV'].value() == True:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Computer list.csv"'
        writer = csv.writer(response)
        writer.writerow(['COMPUTER NAME','IP Address','MAC ADDRESS','USERNAME','LOCATION','PURCHASE DATE','TIMESTAMP'])
        isinstance = queryset
        for row in isinstance:
            writer.writerow([row.computer_name, row.ip_address,row.MAC_address, row.username, row.location, row.purchase_date, row.timestamp])
        return response    
    return render(request , "computer_list.html", context)