
from typing import Any
from django.db import models
from saloon.models import Saloon
from shared.utils import get_context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from incriptions.forms import IncriptionForm
from datetime import datetime

from .models import InformativeOffer, OfferCategory, Topic, SNITCategory, SNITFile

# Create your views here.

def training_index(request):
    camara = request.GET.get('camara', '')
    context = get_context()
    categories = OfferCategory.objects.all()
    context["categories"] = categories
    context["camara"] = camara
    return render(request, "training_categories.html", context)


def training_list(request, category_id):
    context = get_context()
    trainings = InformativeOffer.objects.all().filter(
        category_id=category_id, 
        is_available=True, 
        due_date__gte=datetime.now()
    )
    camara = request.GET.get('camara', '')
    especialidad = request.GET.get('especialidad', '')
    provincia = request.GET.get('provincia', '')
    #import ipdb ; ipdb.set_trace()
    if camara and camara != "null":
        trainings = trainings.filter(saloon_id=int(camara))
    
    if especialidad and especialidad != "null":
        trainings = trainings.filter(topic_id=int(especialidad))
    
    if provincia and provincia != "null":
        trainings = trainings.filter(city=provincia)
    

    training_ids = trainings.values_list('id', flat=True)
    saloon = Saloon.objects.filter(informativeoffer__in=training_ids).distinct()
    topic = Topic.objects.filter(informativeoffer__in=training_ids).distinct()
    cities = trainings.exclude(city=None).values_list("city", flat=True).distinct()
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
        context["form"] = IncriptionForm()
        return context

def process_inscription(request):
    form = IncriptionForm(request.POST)
    form.is_valid()
    form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def snit(request):
    context = get_context()
    context["snits"] = SNITCategory.objects.all()
    return render(request, "snit.html", context)

def snit_detail(request, snit_id):
    context = get_context()
    context["files"] = SNITFile.objects.filter(snit_id=snit_id)
    return render(request, "snit_detail.html", context)