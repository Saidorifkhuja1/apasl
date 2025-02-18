import uuid
from django.db import models
from django.utils import timezone
from speaker.models import Speaker


class Schedule(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=5000)
    time = models.DateTimeField(default=timezone.now)
    speakers = models.ManyToManyField(Speaker)

    def __str__(self):
        return self.title

