from django.contrib import admin
from .models import Speaker

@admin.register(Speaker)
class SSpeakerAdmin(admin.ModelAdmin):
    list_display = ['name']



