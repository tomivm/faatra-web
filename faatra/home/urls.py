from django.urls import path

from . import views

urlpatterns = [
    path("quienes-somos", views.who_we_are, name="who-we-are"),
    path("", views.index, name="index"),
    path(
        "/<slug:url>/",
        views.PagesDetailView.as_view(),
        name="pages-detail",
    ),
]
