from django.db import models
from datetime import datetime

class Squad(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Host(models.Model):
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    mac = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    is_online = models.BooleanField(default=False, blank=True)
    check_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
