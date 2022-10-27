from django.shortcuts import render

def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title":title,
    }
    return render(request , "home.html", context)