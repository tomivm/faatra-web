from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import DateRealization, InformativeOffer, Topic, OfferCategory

from import_export.admin import ExportActionMixin


@admin.register(OfferCategory)
class OfferCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


class DateRealizationInline(admin.TabularInline):
    model = DateRealization


# Register your models here.
@admin.register(InformativeOffer)
class InformativeOfferAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("title", "created_date", "last_modification_date", "is_available")
    inlines = [DateRealizationInline]
    fields = (
        "title",
        "description",
        "content",
        "email_info",
        "image",
        "saloon",
        "city",
        "category",
        "topic",
        "duration",
        "enable_inscription",
        "exhausted",
        "cancelled",
        "is_available",
        "created_date",
        "last_modification_date",
    )
    readonly_fields = ["created_date", "last_modification_date"]
    list_editable = ("is_available",)
    search_fields = ("title",)
    list_filter = ("is_available", "created_date")
