from home.models import SiteConfiguration, SocialMediaConfiguration


def get_context():
    config = SiteConfiguration.objects.get()
    social_config = SocialMediaConfiguration.objects.get()
    context = {"config": config, "social": social_config}

    return context
