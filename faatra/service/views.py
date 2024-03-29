from django.shortcuts import render
from django.views.generic.detail import DetailView

from shared.utils import get_context
from .models import Service

# Create your views here.


class ServiceDetailView(DetailView):
    """Detail service."""

    template_name = "service.html"
    model = Service
    context_object_name = "service"
    slug_field = "url"
    slug_url_kwarg = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = get_context()
        context.update(extra_context)
        return context


def service_index(request, index=0):
    context = get_context()
    services = Service.objects.filter(is_available=True)
    context["services"] = services
    context["index"] = index
    return render(request, "services.html", context)
