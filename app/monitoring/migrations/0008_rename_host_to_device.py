# Generated by Django 4.2.5 on 2023-09-28 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_alter_host_check_date'),
    ]

    operations = [
        migrations.RenameModel('Host', 'Device')
    ]