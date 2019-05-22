from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.conf import settings
import uuid

class HookCall(models.Model):
    body = JSONField()
    item_id = models.CharField(max_length=80, null=True, blank=True)
    webhook_type = models.CharField(max_length=80, null=True, blank=True)
    actionsTaken = ArrayField(models.CharField(max_length=80))
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Request(models.Model):
    path = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session = models.CharField(max_length=80, null=True, blank=True)
    event = models.CharField(max_length=80, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    rid = models.UUIDField(verbose_name="id", default=uuid.uuid4, editable=False)