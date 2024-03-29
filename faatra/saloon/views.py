from django.views.generic.detail import DetailView

from django.shortcuts import render

from shared.utils import get_context
from .models import Saloon


def saloon_home(request):
    context = get_context()
    saloon = Saloon.objects.filter(is_available=True)
    context["saloon"] = saloon
    return render(request, "saloon.html", context)


class SaloonDetailView(DetailView):
    """Detail service."""

    template_name = "saloon-detail.html"
    model = Saloon
    context_object_name = "saloon"
    slug_field = "url"
    slug_url_kwarg = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = get_context()
        context.update(extra_context)
        return context
