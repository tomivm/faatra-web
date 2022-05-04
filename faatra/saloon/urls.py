from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.saloon_home,
        name="saloon-home",
    ),
    path(
        "/<slug:url>/",
        views.SaloonDetailView.as_view(),
        name="saloon-detail",
    ),
]
