from django.contrib import admin

from .models import New, Video

# Register your models here.


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ("title", "created_date", "last_modification_date", "is_available")
    fields = (
        "title",
        "content",
        "image",
        "saloon",
        "course",
        "is_available",
        "created_date",
        "last_modification_date",
    )
    readonly_fields = ["created_date", "last_modification_date"]
    list_editable = ("is_available",)
    search_fields = ("title",)
    list_filter = ("is_available", "created_date")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
