from training.models import InformativeOffer
from saloon.models import ImportantAgreement
from news.models import New
from .models import WhoWeAre, Pages
from shared.utils import get_context

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from service.models import Service

from django.views.generic.detail import DetailView


def index(request):
    context = get_context()
    services = Service.objects.filter(is_available=True).order_by("-created_date")
    pages = Pages.objects.filter(is_available=True, use_in_home=True).order_by("-created_date")
    wwa = WhoWeAre.objects.get()
    context["who_we_are"] = wwa
    context["pages"] = pages
    context["services"] = services
    context["new"] = New.objects.filter(use_in_home=True).order_by("last_modification_date").first()
    context["training"] = InformativeOffer.objects.filter(use_in_home=True).order_by("last_modification_date").first()
    context["agreements"] = ImportantAgreement.objects.filter(is_available=True)
    return render(request, "index.html", context)


def who_we_are(request):
    context = get_context()
    wwa = WhoWeAre.objects.get()
    pages = Pages.objects.filter(is_available=True).order_by("-created_date")
    context["who_we_are"] = wwa
    context["pages"] = pages
    return render(request, "who_we_are.html", context)


class PagesDetailView(DetailView):
    """Detail page."""

    template_name = "pages.html"
    model = Pages
    context_object_name = "page"
    slug_field = "url"
    slug_url_kwarg = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = get_context()
        context.update(extra_context)
        pages = Pages.objects.filter(is_available=True).order_by("-created_date")
        context["pages"] = pages
        return context