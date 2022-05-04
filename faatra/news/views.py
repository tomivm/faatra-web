from django.shortcuts import render

# Create your views here.

from shared.utils import get_context
from .models import New

# Create your views here.


def index(request):
    context = get_context()
    news = New.objects.all()
    context["news"] = news
    return render(request, "news.html", context)
