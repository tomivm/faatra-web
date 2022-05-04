from django.contrib import admin

from saloon.models import Saloon, Link, ImportantAgreement

from import_export.admin import ExportActionMixin

# Register your models here.
@admin.register(Saloon)
class SaloonAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("title", "created_date", "last_modification_date", "is_available")
    fields = (
        "title",
        "complete_name",
        "content",
        "icon",
        "image",
        "address",
        "maps",
        "city",
        "hours",
        "phone",
        "web",
        "email",
        "facebook",
        "is_available",
        "reference",
        "created_date",
        "last_modification_date",
    )
    readonly_fields = ["created_date", "last_modification_date"]
    list_editable = ("is_available",)
    search_fields = ("title",)
    list_filter = ("is_available", "created_date")


@admin.register(ImportantAgreement)
class ImportantAgreementAdmin(admin.ModelAdmin):
    pass
