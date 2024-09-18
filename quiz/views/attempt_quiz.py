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
def attempt_quiz(request, id):
    quiz = QuizModel.objects.get(id=id)
    questions = QuestionModel.objects.filter(quiz=quiz)
    score = 0

    if request.method == "POST":
        user_answers = request.POST.getlist("user_answers[]")
        for index, answer in enumerate(user_answers):
            if questions[index].answer == answer:
                score+=1
        quiz.takers.add(request.user)
        return JsonResponse({"score":score, "total":len(questions)})
    
    return render(request, 'attempt_quiz.html', context={'quiz': quiz, 'questions': questions})