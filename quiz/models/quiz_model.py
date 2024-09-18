from django.db import models
from django.contrib.auth.models import User
from space.models import SpaceModel

class QuizModel(models.Model):
    creator=models.ForeignKey(User, on_delete=models.CASCADE, related_name="quiz")
    space=models.ForeignKey(SpaceModel, on_delete=models.CASCADE, related_name="quiz")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    takers = models.ManyToManyField(User)

#This function is for displaying the title of the spaces in admin panel.
    def __str__(self):
        return str(self.title)