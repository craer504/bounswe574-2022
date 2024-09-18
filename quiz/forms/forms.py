from django import forms
from quiz.models import QuizModel, QuestionModel

class CreateQuizModelForm(forms.ModelForm):
    class Meta:
        model=QuizModel
        fields= ('creator', 'description', 'title')

class CreateQuestionModelForm(forms.ModelForm):
    class Meta:
        model=QuestionModel
        fields= ("__all__")
