from training.models import InformativeOffer
from saloon.models import ImportantAgreement
from news.models import New
from .models import WhoWeAre
from shared.utils import get_context

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from service.models import Service


def index(request):
    context = get_context()
    services = Service.objects.all()
    wwa = WhoWeAre.objects.get()
    context["who_we_are"] = wwa
    context["services"] = services
    context["new"] = New.objects.filter(use_in_home=True).order_by("last_modification_date").first()
    context["training"] = InformativeOffer.objects.filter(use_in_home=True).order_by("last_modification_date").first()
    context["agreements"] = ImportantAgreement.objects.filter(is_available=True)
    return render(request, "index.html", context)


def who_we_are(request):
    context = get_context()
    wwa = WhoWeAre.objects.get()
    context["who_we_are"] = wwa
    return render(request, "who_we_are.html", context)
