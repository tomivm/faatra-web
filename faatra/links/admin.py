from django.contrib import admin

# Register your models here.


from .models import Link

# Register your models here.


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass
