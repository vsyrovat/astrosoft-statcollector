from django.db import models


# Create your models here.
class AccessLogEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=39)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=50)

    class Meta:
        ordering = [models.F("id").desc()]
        verbose_name_plural = "Access log entries"
