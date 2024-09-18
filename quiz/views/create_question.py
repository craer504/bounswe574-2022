from django.shortcuts import redirect, render
from quiz.forms import CreateQuizModelForm, CreateQuestionModelForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quiz.models import QuizModel, QuestionModel
from django.contrib.auth.decorators  import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import JsonResponse
from space.models import SpaceModel

@login_required(login_url='/')
@csrf_exempt
def create_question(request, space_id):
    if request.method == "POST":
        space = SpaceModel.objects.get(id=space_id)
        creator = request.user
        title = request.POST['title']
        description = request.POST['description']
        quiz = QuizModel.objects.create(creator=creator, title=title, description=description, space=space)
        quiz_statements = request.POST.getlist('quizstatements[]')
        quiz_option1 = request.POST.getlist('quizoption1[]')
        quiz_option2 = request.POST.getlist('quizoption2[]')
        quiz_option3 = request.POST.getlist('quizoption3[]')
        quiz_option4 = request.POST.getlist('quizoption4[]')
        answers = request.POST.getlist('answers[]')
        help_links = request.POST.getlist('helplinks[]')

        for index, option1 in enumerate(quiz_option1):
            QuestionModel.objects.create(quiz=quiz, statement=quiz_statements[index], option1=quiz_option1[index],
                                            option2=quiz_option2[index], option3=quiz_option3[index], 
                                            option4=quiz_option4[index],  answer=answers[index], help_link=help_links[index] if help_links[index] is not '' else None)
    
    return render(request,'create-question.html', context={'space_id':space_id})