from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

# Create your views here.

from shared.utils import get_context
from .models import New

# Create your views here.


def index(request):
    context = get_context()
    camara = request.GET.get('camara', '')
    news = New.objects.filter(is_available=True).order_by("-created_date")

    if camara and camara != "null":
        news = news.filter(saloon_id=int(camara))

    paginator = Paginator(news, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context["news"] = page_obj
    context["numbers"] = [number+1 for number in range(page_obj.paginator.num_pages)]
    return render(request, "news.html", context)


class NewDetailView(DetailView):
    """Detail new."""

    template_name = "new.html"
    model = New
    context_object_name = "new"
    slug_field = "url"
    slug_url_kwarg = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = get_context()
        context.update(extra_context)
        return context