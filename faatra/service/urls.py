from django.urls import path

from . import views

urlpatterns = [
    path(
        "/<slug:url>/",
        views.ServiceDetailView.as_view(),
        name="service-detail",
    ),
    path(
        "/",
        views.service_index,
        name="services",
    ),
     path(
        "/<int:index>",
        views.service_index,
        name="service-index",
    ),
]
