from django.contrib import admin
from .models import Host, Squad

class HostInline(admin.TabularInline ):
    model = Host
    extra = 0
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Network information", {"fields": ["ip", "mac", "hostname"], "classes": ["collapse"]}),
        ("Other", {"fields": ["description"], "classes": ["collapse"]}),
    ]

class SquadAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "priority"]}),
    ]
    inlines = [HostInline]
    search_fields = ["name"]
    list_display = ["name", "priority"]

admin.site.register(Squad, SquadAdmin)
