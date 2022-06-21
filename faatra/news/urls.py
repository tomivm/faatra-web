from django.urls import path

from . import views


urlpatterns = [
    path(
        "/<slug:url>/",
        views.NewDetailView.as_view(),
        name="new-detail",
    ),
    path("", views.index, name="news"),
]
