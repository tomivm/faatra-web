from shared.utils import get_context

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

from service.models import Service
from .models import SiteConfiguration, SocialMediaConfiguration


def index(request):
    context = get_context()
    services = Service.objects.all()
    context["services"] = services
    return render(request, "index.html", context)
