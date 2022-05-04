from django.shortcuts import render

from django.shortcuts import render

from shared.utils import get_context
from .models import Saloon


def saloon_home(request):
    context = get_context()
    saloon = Saloon.objects.all()
    context["saloon"] = saloon
    return render(request, "saloon.html", context)
