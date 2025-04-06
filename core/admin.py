from django.contrib import admin
from .models import RadioFM


@admin.register(RadioFM)
class RadioFMAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'listeners')
