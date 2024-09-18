from django.shortcuts import redirect, render
from quiz.forms import CreateQuizModelForm, CreateQuestionModelForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz.models import QuizModel, QuestionModel
from django.contrib.auth.decorators  import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import JsonResponse


@login_required(login_url='/')
@csrf_exempt
def create_quiz(request):
    
    form=CreateQuizModelForm(request.POST or None, files=request.FILES or None)
    
    if form.is_valid():
        quiz=form.save()
    
    return render(request,'create-quiz.html', context={'form':form})