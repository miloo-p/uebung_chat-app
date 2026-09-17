from django.db import models
from django.utils import timezone

# Create your models here.


class Chat (models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=300, blank=True, default="")
    created_at = models.DateTimeField(default=timezone.now)
