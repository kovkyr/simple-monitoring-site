from django.http import HttpResponse
from django.shortcuts import render
from .models import Squad, Device
from datetime import datetime

def index(request):
    devices = Device.objects.order_by('-squad__priority', 'squad__name', 'name')
    squads = Squad.objects.order_by('-priority')
    context = { "devices": devices, "squads": squads,  "date": datetime.now() }
    return render(request, "monitoring/index.html", context)

def table(request):
    devices = Device.objects.order_by('-squad__priority', 'squad__name', 'name')
    context = { "devices": devices, "date": datetime.now() }
    return render(request, "monitoring/table.html", context)
