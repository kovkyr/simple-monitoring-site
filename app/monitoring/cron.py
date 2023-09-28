import os
import time
from datetime import datetime
from django.utils import timezone
from .models import Squad, Host
import django

def check_host_is_online(ip):
    stream = os.popen("ping -c1 -W1 %s > /dev/null && echo 'Online' || echo 'Offline' | tail -n 1" % ip)
    output = stream.read()
    output = output.strip()
    return output == 'Online'

def check_hosts():
    hosts = Host.objects.all()
    for host in hosts:
        is_host_online = check_host_is_online(host.ip)
        message = ''
        if is_host_online:
            host.is_online = True
            host.check_date = timezone.now()
            host.save()
        else:
            host.is_online = False
            host.check_date = timezone.now()
            host.save()
