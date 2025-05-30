from django.core.cache import cache
from home.models import SiteConfiguration, SocialMediaConfiguration


def get_context():
    # Cache the context for 10 minutes since this data rarely changes
    cache_key = 'site_context'
    context = cache.get(cache_key)
    
    if context is None:
        try:
            config = SiteConfiguration.objects.first()
            social_config = SocialMediaConfiguration.objects.first()
            context = {"config": config, "social": social_config}
            # Cache for 10 minutes (600 seconds)
            cache.set(cache_key, context, 600)
        except (SiteConfiguration.DoesNotExist, SocialMediaConfiguration.DoesNotExist):
            # Fallback in case objects don't exist
            context = {"config": None, "social": None}
            cache.set(cache_key, context, 60)  # Cache shorter for missing data
    
    return context
