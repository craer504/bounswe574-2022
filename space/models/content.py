from django.db import models
from django.contrib.auth.models import User
from space.models import SpaceModel

class ContentModel(models.Model):
    title = models.CharField(max_length=200)
    space=models.ForeignKey(SpaceModel, on_delete=models.CASCADE, blank=True)
    created_time=models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    creator=models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=300,default=None, blank=True, null=True)
    def __str__(self):
        return self.title