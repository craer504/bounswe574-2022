from django.db import models
from django.contrib.auth.models import User
from .quiz_model import QuizModel

class QuestionModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name="question")
    statement = models.CharField(max_length=300)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=100, null=True, blank=True)
    help_link = models.URLField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.statement)