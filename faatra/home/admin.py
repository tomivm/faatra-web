from django.contrib import admin

# Register your models here.

from django.contrib import admin
from home.models import WhoWeAre
from solo.admin import SingletonModelAdmin
from home.models import SiteConfiguration, SocialMediaConfiguration, Pages


admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(SocialMediaConfiguration, SingletonModelAdmin)
admin.site.register(WhoWeAre, SingletonModelAdmin)

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ("title", "created_date", "last_modification_date", "is_available")
    fields = (
        "title",
        "description",
        "content",
        "image",
        "icon",
        "is_available",
        "created_date",
        "last_modification_date",
        "use_in_home",
        
    )
    readonly_fields = ["created_date", "last_modification_date"]
    list_editable = ("is_available",)
    search_fields = ("title",)
    list_filter = ("is_available", "created_date")

