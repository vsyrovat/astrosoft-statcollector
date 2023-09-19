from django.contrib import admin

from .models import AccessLogEntry


@admin.register(AccessLogEntry)
class AccessLogEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "ip", "user_agent", "accept_language"]
