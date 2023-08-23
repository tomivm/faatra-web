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
        "/snit",
        views.snit,
        name="snit-list",
    ),
     path(
        "/snit/<int:snit_id>",
        views.snit_detail,
        name="snit-detail",
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
