from django.db import models
from django.contrib.auth.models import User
from space.models import SpaceModel
from space.models.content import ContentModel


class RelationModel(models.Model):
    source_content = models.ForeignKey(ContentModel, related_name="source_content", on_delete=models.CASCADE)
    target_content = models.ForeignKey(ContentModel, related_name="target_content" ,on_delete=models.CASCADE)
    space=models.ForeignKey(SpaceModel, on_delete=models.CASCADE, blank=True)
    created_time=models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    creator=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title