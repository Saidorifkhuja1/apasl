from django.db import models
import uuid

class Organiser(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='organiser/', blank=True, null=True)
    role = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name
