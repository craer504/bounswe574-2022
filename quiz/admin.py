from django.contrib import admin
from .models import QuizModel, QuestionModel
# Register your models here.

admin.site.register(QuestionModel)
admin.site.register(QuizModel)
