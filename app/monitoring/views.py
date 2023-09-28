from django.http import HttpResponse
from django.shortcuts import render
from .models import Squad, Host
from datetime import datetime

def index(request):
    hosts = Host.objects.order_by('-squad__priority', 'squad__name', 'name')
    context = { "hosts": hosts, "date": datetime.now() }
    return render(request, "monitoring/index.html", context)
