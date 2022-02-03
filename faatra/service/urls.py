from django.urls import path

from . import views

urlpatterns = [
    path(
        "/<slug:url>/",
        views.ServiceDetailView.as_view(),
        name="service-detail",
    ),
]
