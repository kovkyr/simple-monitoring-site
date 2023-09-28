from django.http import HttpResponse
from django.shortcuts import render
from .models import Squad, Device
from datetime import datetime

def index(request):
    devices = Device.objects.order_by('-squad__priority', 'squad__name', 'name')
    context = { "devices": devices, "date": datetime.now() }
    return render(request, "monitoring/index.html", context)
