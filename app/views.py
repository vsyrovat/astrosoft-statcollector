import json
from time import time

from django.http import HttpResponse
from django.shortcuts import render

from .models import AccessLogEntry


# Create your views here.
def index(request):
    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    AccessLogEntry.objects.create(
        ip=get_client_ip(request),
        user_agent=request.user_agent,
        accept_language=request.META.get("HTTP_ACCEPT_LANGUAGE"),
    )

    data = {"ts": time() * 1000}
    return HttpResponse(json.dumps(data), content_type="application/json")
