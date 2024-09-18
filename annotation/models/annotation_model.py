from django.db import models
from django.contrib.auth.models import User


class AnnotationModel(models.Model):
    annotation = models.JSONField()
    def __str__(self):
        return str(self.annotation)