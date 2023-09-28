# Generated by Django 4.2.5 on 2023-09-28 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_squad_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='check_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='host',
            name='is_online',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
