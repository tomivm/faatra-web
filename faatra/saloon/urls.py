from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.saloon_home,
        name="saloon-home",
    ),
]
