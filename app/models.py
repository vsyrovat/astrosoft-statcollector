import re

from django.db import models
from django.utils.html import format_html


# Create your models here.
class AccessLogEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=39)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=50, null=True)

    def flag(self):
        country_code = re.search(r"[a-z]+", self.accept_language, flags=re.IGNORECASE)[
            0
        ].upper()
        if country_code == "EN":
            country_code = "GBR"
        return format_html(f'<img src="/static/flags/{country_code}.svg">')

    flag.short_description = "Accept Language"

    class Meta:
        ordering = [models.F("id").desc()]
        verbose_name_plural = "Access log entries"
