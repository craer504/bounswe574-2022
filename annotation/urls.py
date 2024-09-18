from django.urls import path
from .views import (
    create_annotation,
    get_annotations,
    delete_annotation,
    update_annotation
)
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("api/create-annotation/", create_annotation, name="create_annotation"),
    path("api/get-annotations/", get_annotations, name="get_annotations"),
    path("api/delete-annotation/", delete_annotation, name="delete-annotation"),
    path("api/update-annotation/", update_annotation, name="update-annotation"),
]
