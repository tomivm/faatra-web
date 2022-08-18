from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

# Create your views here.

from shared.utils import get_context
from .models import New

# Create your views here.


def index(request):
    context = get_context()
    news = New.objects.all()
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context["news"] = page_obj
    context["numbers"] = range(page_obj.paginator.num_pages)
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