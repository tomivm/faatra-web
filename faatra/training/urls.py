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
        "/process-inscription",
        views.process_inscription,
        name="process-inscription",
    ),
     path(
        "/<slug:url>",
        views.TrainingDetailView.as_view(),
        name="traning-detail",
    ),
]
