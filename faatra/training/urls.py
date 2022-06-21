from django.urls import path

from . import views

urlpatterns = [
    path(
        "/",
        views.training_index,
        name="training",
    ),
    path(
        "/<int:category_id>",
        views.training_list,
        name="training-list",
    ),
     path(
        "/<slug:url>",
        views.TrainingDetailView.as_view(),
        name="traning-detail",
    ),
]
