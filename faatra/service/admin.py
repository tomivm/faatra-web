from pyexpat import model
from django.contrib import admin

# Register your models here.
from .models import Service, Files

from import_export.admin import ExportActionMixin


class FilesAdmin(admin.TabularInline):
    model = Files



@admin.register(Service)
class ServiceAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("title", "created_date", "last_modification_date", "is_available")
    fields = (
        "title",
        "description",
        "content",
        "image",
        "icon",
        "created_date",
        "last_modification_date",
        "is_available",
    )
    readonly_fields = ["created_date", "last_modification_date"]
    list_editable = ("is_available",)
    search_fields = ("title",)
    list_filter = ("is_available", "created_date")
    inlines = [FilesAdmin]
