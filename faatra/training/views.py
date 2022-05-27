
from shared.utils import get_context
from django.shortcuts import render

from .models import OfferCategory

# Create your views here.

def training_index(request):
    context = get_context()
    categories = OfferCategory.objects.all()
    context["categories"] = categories
    return render(request, "training_categories.html", context)
