from django.contrib import admin

# Register your models here.


from .models import Partnership

# Register your models here.


@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    pass
