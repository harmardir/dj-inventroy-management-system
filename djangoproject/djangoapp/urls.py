from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('computer_entry', views.computer_entry, name='computer_entry'),
]