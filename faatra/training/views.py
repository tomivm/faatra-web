
from saloon.models import Saloon
from shared.utils import get_context
from django.shortcuts import render
from django.views.generic.detail import DetailView


from .models import InformativeOffer, OfferCategory, Topic

# Create your views here.

def training_index(request):
    context = get_context()
    categories = OfferCategory.objects.all()
    context["categories"] = categories
    return render(request, "training_categories.html", context)


def training_list(request, category_id):
    context = get_context()
    trainings = InformativeOffer.objects.all().filter(category_id=category_id)
    
    camara = request.GET.get('camara', '')
    especialidad = request.GET.get('especialidad', '')
    provincia = request.GET.get('provincia', '')

    if camara and camara != "null":
        trainings.filter(saloon_id=camara)
    
    if especialidad and especialidad != "null":
        trainings.filter(topic=especialidad)
    
    if provincia and provincia != "null":
        trainings.filter(city=provincia)
    
    training_ids = trainings.values_list('id', flat=True)
    saloon = Saloon.objects.filter(informativeoffer__in=training_ids)
    topic = Topic.objects.filter(informativeoffer__in=training_ids)
    cities = trainings.values_list("city", flat=True)
    context["tranings"] = trainings
    context["saloon"] = saloon
    context["topic"] = topic
    context["cities"] = cities
    return render(request, "training_categories_filter.html", context)


class TrainingDetailView(DetailView):
    """Detail training."""

    template_name = "traning-detail.html"
    model = InformativeOffer
    context_object_name = "training"
    slug_field = "url"
    slug_url_kwarg = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = get_context()
        context.update(extra_context)
        return context
