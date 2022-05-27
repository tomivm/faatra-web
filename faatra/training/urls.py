from django.urls import path

from . import views

urlpatterns = [
    path(
        "/",
        views.training_index,
        name="training",
    ),
]
