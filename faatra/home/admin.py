from django.contrib import admin

# Register your models here.

from django.contrib import admin
from home.models import WhoWeAre
from solo.admin import SingletonModelAdmin
from home.models import SiteConfiguration, SocialMediaConfiguration


admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(SocialMediaConfiguration, SingletonModelAdmin)
admin.site.register(WhoWeAre, SingletonModelAdmin)
