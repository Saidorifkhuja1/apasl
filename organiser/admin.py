from django.contrib import admin
from .models import Organiser

@admin.register(Organiser)
class OrganiserAdmin(admin.ModelAdmin):
    list_display = ['name']