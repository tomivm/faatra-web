from os import link
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from shared.utils import get_context
from .models import Link

# Create your views here.


def index(request):
    context = get_context()
    links = Link.objects.all()
    context["links"] = links
    return render(request, "links.html", context)
