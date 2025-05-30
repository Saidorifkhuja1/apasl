import uuid
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from speaker.models import Speaker


def validate_file_extension(value):
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
        raise ValidationError("Only PDF and DOC/DOCX files are allowed.")


class Schedule(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=5000)
    time = models.DateTimeField(default=timezone.now)
    speakers = models.ManyToManyField(Speaker)
    file = models.FileField(
        upload_to='schedule_files/',
        validators=[validate_file_extension],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
