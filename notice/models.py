from django.db import models
from django.utils import timezone


class Notice(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(
            default=timezone.now)