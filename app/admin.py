from django.contrib import admin
from django.http.request import HttpRequest

from .models import AccessLogEntry


@admin.register(AccessLogEntry)
class AccessLogEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "ip", "user_agent", "flag"]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
