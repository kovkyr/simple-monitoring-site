import os
import time
from datetime import datetime
from django.utils import timezone
from .models import Squad, Device
import django

def check_device_is_online(ip):
    stream = os.popen("ping -c1 -W1 %s > /dev/null && echo 'Online' || echo 'Offline' | tail -n 1" % ip)
    output = stream.read()
    output = output.strip()
    return output == 'Online'

def check_devices():
    devices = Device.objects.order_by('-squad__priority', 'squad__name', 'name')
    for device in devices:
        is_device_online = check_device_is_online(device.ip)
        message = ''
        if is_device_online:
            device.is_online = True
            device.check_date = timezone.now()
            device.save()
        else:
            device.is_online = False
            device.check_date = timezone.now()
            device.save()
